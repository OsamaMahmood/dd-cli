"""Import scanner findings into DefectDojo.

Two modes, picked by `auto_create_context`:

1. **Traditional** — find-or-create the product type, product, engagement,
   and test, then upload the scan to that test.
2. **Auto-create** — single POST to ``/api/v2/reimport-scan/`` with
   ``auto_create_context: true`` letting DefectDojo create everything.

Both branches preserve the behavior of the original `dd-import` tool;
every `DD_*` env var the legacy `Environment` class read is honored as
a `pydantic-settings` validation alias on `ImportFindingsOptions`, so
the legacy console scripts (`dd-reimport-findings`) can be wired as a
thin shim over `ImportFindingsWorkflow.run()` in M4b.
"""

from __future__ import annotations

import datetime as _dt
from collections.abc import Mapping
from itertools import islice
from pathlib import Path
from typing import Any

from pydantic import AliasChoices, ConfigDict, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from dd_cli.client import DefectDojoClient
from dd_cli.errors import APIError, ConfigError, ValidationError

VALID_BUSINESS_CRITICALITIES = {
    "very high",
    "high",
    "medium",
    "low",
    "very low",
    "none",
}
VALID_PLATFORMS = {"web service", "desktop", "iot", "mobile", "web"}
VALID_LIFECYCLES = {"construction", "production", "retirement"}


def _today_iso() -> str:
    return _dt.date.today().isoformat()


def _split_csv(value: str | None) -> list[str]:
    if not value:
        return []
    return [t.strip() for t in value.split(",") if t.strip()]


class ImportFindingsOptions(BaseSettings):
    """All knobs for an import. Reads from CLI flags + DD_* env vars + defaults.

    Each field declares a `validation_alias` covering the legacy `DD_*`
    name that the original `dd-import` `Environment` class read, plus
    (where appropriate) a new `DD_CLI_*` form. CLI invocation passes
    explicit values; the legacy shim in M4b calls this with no overrides
    and lets env-var aliases take effect.
    """

    model_config = SettingsConfigDict(
        case_sensitive=False,
        extra="ignore",
        populate_by_name=True,
    )

    # --- core scan + scoping ---------------------------------------------- #
    file: Path | None = Field(
        default=None,
        validation_alias=AliasChoices("DD_CLI_FILE", "DD_FILE_NAME"),
    )
    scanner: str | None = Field(
        default=None,
        validation_alias=AliasChoices("DD_CLI_SCANNER", "DD_TEST_TYPE_NAME"),
    )
    product_type_name: str | None = Field(
        default=None,
        validation_alias=AliasChoices("DD_CLI_PRODUCT_TYPE", "DD_PRODUCT_TYPE_NAME"),
    )
    product_name: str | None = Field(
        default=None,
        validation_alias=AliasChoices("DD_CLI_PRODUCT", "DD_PRODUCT_NAME"),
    )
    engagement_name: str | None = Field(
        default=None,
        validation_alias=AliasChoices("DD_CLI_ENGAGEMENT", "DD_ENGAGEMENT_NAME"),
    )
    test_name: str | None = Field(
        default=None,
        validation_alias=AliasChoices("DD_CLI_TEST_NAME", "DD_TEST_NAME"),
    )
    auto_create_context: bool = Field(
        default=False,
        validation_alias=AliasChoices(
            "DD_CLI_AUTO_CREATE_CONTEXT",
            "DD_AUTO_CREATE_CONTEXT",
        ),
    )

    # --- engagement targeting --------------------------------------------- #
    engagement_target_start: str = Field(
        default_factory=_today_iso,
        validation_alias=AliasChoices(
            "DD_CLI_ENGAGEMENT_TARGET_START",
            "DD_ENGAGEMENT_TARGET_START",
        ),
    )
    engagement_target_end: str = Field(
        default="2999-12-31",
        validation_alias=AliasChoices(
            "DD_CLI_ENGAGEMENT_TARGET_END",
            "DD_ENGAGEMENT_TARGET_END",
        ),
    )

    # --- scan flags ------------------------------------------------------- #
    active: bool = Field(default=True, validation_alias=AliasChoices("DD_ACTIVE"))
    verified: bool = Field(default=True, validation_alias=AliasChoices("DD_VERIFIED"))
    minimum_severity: str | None = Field(
        default=None, validation_alias=AliasChoices("DD_MINIMUM_SEVERITY")
    )
    push_to_jira: bool = Field(default=False, validation_alias=AliasChoices("DD_PUSH_TO_JIRA"))
    close_old_findings: bool = Field(
        default=True, validation_alias=AliasChoices("DD_CLOSE_OLD_FINDINGS")
    )
    close_old_findings_product_scope: bool = Field(
        default=False,
        validation_alias=AliasChoices("DD_CLOSE_OLD_FINDINGS_PRODUCT_SCOPE"),
    )
    do_not_reactivate: bool = Field(
        default=False, validation_alias=AliasChoices("DD_DO_NOT_REACTIVATE")
    )
    deduplication_on_engagement: bool = Field(
        default=False,
        validation_alias=AliasChoices("DD_DEDUPLICATION_ON_ENGAGEMENT"),
    )

    # --- build context ---------------------------------------------------- #
    version: str | None = Field(default=None, validation_alias=AliasChoices("DD_VERSION"))
    build_id: str | None = Field(default=None, validation_alias=AliasChoices("DD_BUILD_ID"))
    commit_hash: str | None = Field(default=None, validation_alias=AliasChoices("DD_COMMIT_HASH"))
    branch_tag: str | None = Field(default=None, validation_alias=AliasChoices("DD_BRANCH_TAG"))

    # --- scoping helpers -------------------------------------------------- #
    endpoint_id: int | None = Field(default=None, validation_alias=AliasChoices("DD_ENDPOINT_ID"))
    service: str | None = Field(default=None, validation_alias=AliasChoices("DD_SERVICE"))
    api_scan_configuration_id: int | None = Field(
        default=None, validation_alias=AliasChoices("DD_API_SCAN_CONFIGURATION_ID")
    )
    source_code_management_uri: str | None = Field(
        default=None, validation_alias=AliasChoices("DD_SOURCE_CODE_MANAGEMENT_URI")
    )
    group_by: str | None = Field(default=None, validation_alias=AliasChoices("DD_GROUP_BY"))

    # --- product metadata (auto-create + traditional new_product) -------- #
    product_description: str | None = Field(
        default=None, validation_alias=AliasChoices("DD_PRODUCT_DESCRIPTION")
    )
    product_business_criticality: str | None = Field(
        default=None,
        validation_alias=AliasChoices("DD_PRODUCT_BUSINESS_CRITICALITY"),
    )
    product_platform: str | None = Field(
        default=None, validation_alias=AliasChoices("DD_PRODUCT_PLATFORM")
    )
    product_lifecycle: str | None = Field(
        default=None, validation_alias=AliasChoices("DD_PRODUCT_LIFECYCLE")
    )
    product_origin: str | None = Field(
        default=None, validation_alias=AliasChoices("DD_PRODUCT_ORIGIN")
    )
    product_user_records: int | None = Field(
        default=None, validation_alias=AliasChoices("DD_PRODUCT_USER_RECORDS")
    )
    product_revenue: str | None = Field(
        default=None, validation_alias=AliasChoices("DD_PRODUCT_REVENUE")
    )
    product_external_audience: bool = Field(
        default=False,
        validation_alias=AliasChoices("DD_PRODUCT_EXTERNAL_AUDIENCE"),
    )
    product_internet_accessible: bool = Field(
        default=False,
        validation_alias=AliasChoices("DD_PRODUCT_INTERNET_ACCESSIBLE"),
    )
    product_enable_simple_risk_acceptance: bool = Field(
        default=True,
        validation_alias=AliasChoices("DD_PRODUCT_ENABLE_SIMPLE_RISK_ACCEPTANCE"),
    )
    product_enable_full_risk_acceptance: bool = Field(
        default=False,
        validation_alias=AliasChoices("DD_PRODUCT_ENABLE_FULL_RISK_ACCEPTANCE"),
    )
    product_tags: str | None = Field(default=None, validation_alias=AliasChoices("DD_PRODUCT_TAGS"))

    # --- product-type metadata ------------------------------------------- #
    product_type_description: str | None = Field(
        default=None,
        validation_alias=AliasChoices("DD_PRODUCT_TYPE_DESCRIPTION"),
    )
    product_type_critical_product: bool = Field(
        default=False,
        validation_alias=AliasChoices("DD_PRODUCT_TYPE_CRITICAL_PRODUCT"),
    )
    product_type_key_product: bool = Field(
        default=False,
        validation_alias=AliasChoices("DD_PRODUCT_TYPE_KEY_PRODUCT"),
    )

    # --- engagement metadata --------------------------------------------- #
    engagement_description: str | None = Field(
        default=None, validation_alias=AliasChoices("DD_ENGAGEMENT_DESCRIPTION")
    )
    engagement_version: str | None = Field(
        default=None, validation_alias=AliasChoices("DD_ENGAGEMENT_VERSION")
    )
    engagement_first_contacted: str | None = Field(
        default=None, validation_alias=AliasChoices("DD_ENGAGEMENT_FIRST_CONTACTED")
    )
    engagement_reason: str | None = Field(
        default=None, validation_alias=AliasChoices("DD_ENGAGEMENT_REASON")
    )
    engagement_tracker: str | None = Field(
        default=None, validation_alias=AliasChoices("DD_ENGAGEMENT_TRACKER")
    )
    engagement_test_strategy: str | None = Field(
        default=None, validation_alias=AliasChoices("DD_ENGAGEMENT_TEST_STRATEGY")
    )
    engagement_threat_model: bool = Field(
        default=False, validation_alias=AliasChoices("DD_ENGAGEMENT_THREAT_MODEL")
    )
    engagement_api_test: bool = Field(
        default=False, validation_alias=AliasChoices("DD_ENGAGEMENT_API_TEST")
    )
    engagement_pen_test: bool = Field(
        default=False, validation_alias=AliasChoices("DD_ENGAGEMENT_PEN_TEST")
    )
    engagement_check_list: bool = Field(
        default=False, validation_alias=AliasChoices("DD_ENGAGEMENT_CHECK_LIST")
    )
    engagement_status: str = Field(
        default="In Progress",
        validation_alias=AliasChoices("DD_ENGAGEMENT_STATUS"),
    )
    engagement_tags: str | None = Field(
        default=None, validation_alias=AliasChoices("DD_ENGAGEMENT_TAGS")
    )

    # --- test metadata --------------------------------------------------- #
    test_description: str | None = Field(
        default=None, validation_alias=AliasChoices("DD_TEST_DESCRIPTION")
    )
    test_version: str | None = Field(default=None, validation_alias=AliasChoices("DD_TEST_VERSION"))
    test_tags: str | None = Field(default=None, validation_alias=AliasChoices("DD_TEST_TAGS"))
    test_environment_name: str | None = Field(
        default=None, validation_alias=AliasChoices("DD_TEST_ENVIRONMENT_NAME")
    )

    # --- finding controls + tagging -------------------------------------- #
    apply_tags_to_findings: bool = Field(
        default=False, validation_alias=AliasChoices("DD_APPLY_TAGS_TO_FINDINGS")
    )
    apply_tags_to_endpoints: bool = Field(
        default=False, validation_alias=AliasChoices("DD_APPLY_TAGS_TO_ENDPOINTS")
    )
    create_finding_groups_for_all_findings: bool = Field(
        default=True,
        validation_alias=AliasChoices("DD_CREATE_FINDING_GROUPS_FOR_ALL_FINDINGS"),
    )
    finding_tags: str | None = Field(default=None, validation_alias=AliasChoices("DD_FINDING_TAGS"))
    lead: int | None = Field(default=None, validation_alias=AliasChoices("DD_LEAD"))


class ImportFindingsWorkflow:
    """Run a finding import end-to-end against a DefectDojoClient."""

    def __init__(self, client: DefectDojoClient, opts: ImportFindingsOptions) -> None:
        self._client = client
        self._opts = opts
        self._validate()

    # ------------------------------------------------------------------ #
    #  Public                                                            #
    # ------------------------------------------------------------------ #

    def run(self) -> dict[str, Any]:
        """Execute the import. Returns the parsed response from DefectDojo."""
        if self._opts.auto_create_context:
            return self._run_auto_create()
        return self._run_traditional()

    # ------------------------------------------------------------------ #
    #  Validation                                                        #
    # ------------------------------------------------------------------ #

    def _validate(self) -> None:
        opts = self._opts
        missing: list[str] = []
        if not opts.product_type_name:
            missing.append("product_type")
        if not opts.product_name:
            missing.append("product")
        if not opts.scanner:
            missing.append("scanner")

        if not opts.auto_create_context:
            if not opts.engagement_name:
                missing.append("engagement")
            if not opts.test_name:
                missing.append("test_name")

        if missing:
            raise ConfigError(
                f"Missing required option(s) for import: {', '.join(missing)}",
                hint=(
                    "Pass them as CLI flags (e.g. --product-type, --product, "
                    "--scanner) or set the matching DD_* env vars."
                ),
            )

        if opts.product_business_criticality and (
            opts.product_business_criticality not in VALID_BUSINESS_CRITICALITIES
        ):
            raise ValidationError(
                f"product_business_criticality must be one of "
                f"{sorted(VALID_BUSINESS_CRITICALITIES)}",
            )
        if opts.product_platform and opts.product_platform not in VALID_PLATFORMS:
            raise ValidationError(
                f"product_platform must be one of {sorted(VALID_PLATFORMS)}",
            )
        if opts.product_lifecycle and opts.product_lifecycle not in VALID_LIFECYCLES:
            raise ValidationError(
                f"product_lifecycle must be one of {sorted(VALID_LIFECYCLES)}",
            )

    # ------------------------------------------------------------------ #
    #  Traditional workflow                                              #
    # ------------------------------------------------------------------ #

    def _run_traditional(self) -> dict[str, Any]:
        product_type_id = self._find_or_create_product_type()
        product_id = self._find_or_create_product(product_type_id)
        engagement_id = self._find_or_create_engagement(product_id)
        test_id = self._find_or_create_test(engagement_id)
        body = self._reimport(test_id=test_id)
        self._update_engagement_build_metadata(engagement_id)
        return body

    def _find_or_create_product_type(self) -> int:
        opts = self._opts
        for item in islice(
            self._client.paginate(
                "/api/v2/product_types/", params={"name": opts.product_type_name}
            ),
            100,
        ):
            if item.get("name") == opts.product_type_name:
                pt_id = item.get("id")
                if isinstance(pt_id, int):
                    return pt_id
        payload: dict[str, Any] = {"name": opts.product_type_name}
        if opts.product_type_description is not None:
            payload["description"] = opts.product_type_description
        if opts.product_type_critical_product:
            payload["critical_product"] = True
        if opts.product_type_key_product:
            payload["key_product"] = True
        body = self._client.post("/api/v2/product_types/", json=payload)
        new_id = body.get("id")
        if not isinstance(new_id, int):
            raise APIError("New product type missing integer id")
        return new_id

    def _find_or_create_product(self, product_type_id: int) -> int:
        opts = self._opts
        for item in islice(
            self._client.paginate(
                "/api/v2/products/",
                params={"name": opts.product_name, "prod_type": product_type_id},
            ),
            100,
        ):
            if item.get("name") == opts.product_name:
                pid = item.get("id")
                if isinstance(pid, int):
                    return pid
        payload: dict[str, Any] = {
            "name": opts.product_name,
            "description": opts.product_description or opts.product_name,
            "prod_type": product_type_id,
        }
        for src, key in (
            ("product_business_criticality", "business_criticality"),
            ("product_platform", "platform"),
            ("product_lifecycle", "lifecycle"),
            ("product_origin", "origin"),
            ("product_revenue", "revenue"),
        ):
            value = getattr(opts, src)
            if value is not None:
                payload[key] = value
        if opts.product_user_records is not None:
            payload["user_records"] = opts.product_user_records
        if opts.product_external_audience:
            payload["external_audience"] = True
        if opts.product_internet_accessible:
            payload["internet_accessible"] = True
        if opts.product_enable_simple_risk_acceptance is False:
            payload["enable_simple_risk_acceptance"] = False
        if opts.product_enable_full_risk_acceptance:
            payload["enable_full_risk_acceptance"] = True
        tags = _split_csv(opts.product_tags)
        if tags:
            payload["tags"] = tags
        body = self._client.post("/api/v2/products/", json=payload)
        new_id = body.get("id")
        if not isinstance(new_id, int):
            raise APIError("New product missing integer id")
        return new_id

    def _find_or_create_engagement(self, product_id: int) -> int:
        opts = self._opts
        for item in islice(
            self._client.paginate(
                "/api/v2/engagements/",
                params={"name": opts.engagement_name, "product": product_id},
            ),
            100,
        ):
            if item.get("name") == opts.engagement_name:
                eid = item.get("id")
                if isinstance(eid, int):
                    return eid
        payload: dict[str, Any] = {
            "name": opts.engagement_name,
            "product": product_id,
            "target_start": opts.engagement_target_start,
            "target_end": opts.engagement_target_end,
            "engagement_type": "CI/CD",
            "status": opts.engagement_status,
        }
        for src, key in (
            ("engagement_description", "description"),
            ("engagement_version", "version"),
            ("engagement_first_contacted", "first_contacted"),
            ("engagement_reason", "reason"),
            ("engagement_tracker", "tracker"),
            ("engagement_test_strategy", "test_strategy"),
            ("source_code_management_uri", "source_code_management_uri"),
        ):
            value = getattr(opts, src)
            if value is not None:
                payload[key] = value
        for src, key in (
            ("engagement_threat_model", "threat_model"),
            ("engagement_api_test", "api_test"),
            ("engagement_pen_test", "pen_test"),
            ("engagement_check_list", "check_list"),
        ):
            if getattr(opts, src):
                payload[key] = True
        tags = _split_csv(opts.engagement_tags)
        if tags:
            payload["tags"] = tags
        body = self._client.post("/api/v2/engagements/", json=payload)
        new_id = body.get("id")
        if not isinstance(new_id, int):
            raise APIError("New engagement missing integer id")
        return new_id

    def _find_or_create_test(self, engagement_id: int) -> int:
        opts = self._opts
        for item in islice(
            self._client.paginate(
                "/api/v2/tests/",
                params={"title": opts.test_name, "engagement": engagement_id},
            ),
            100,
        ):
            if item.get("title") == opts.test_name:
                tid = item.get("id")
                if isinstance(tid, int):
                    return tid

        test_type_id = self._resolve_test_type_id()
        today = _today_iso()
        payload: dict[str, Any] = {
            "title": opts.test_name,
            "engagement": engagement_id,
            "target_start": today,
            "target_end": "2999-12-31",
            "test_type": test_type_id,
        }
        for src, key in (
            ("test_description", "description"),
            ("test_version", "version"),
            ("build_id", "build_id"),
            ("commit_hash", "commit_hash"),
            ("branch_tag", "branch_tag"),
        ):
            value = getattr(opts, src)
            if value is not None:
                payload[key] = value
        if opts.lead is not None:
            payload["lead"] = opts.lead
        if opts.api_scan_configuration_id is not None:
            payload["api_scan_configuration"] = opts.api_scan_configuration_id
        tags = _split_csv(opts.test_tags)
        if tags:
            payload["tags"] = tags
        body = self._client.post("/api/v2/tests/", json=payload)
        new_id = body.get("id")
        if not isinstance(new_id, int):
            raise APIError("New test missing integer id")
        return new_id

    def _resolve_test_type_id(self) -> int:
        opts = self._opts
        for item in islice(
            self._client.paginate("/api/v2/test_types/", params={"name": opts.scanner}),
            100,
        ):
            if item.get("name") == opts.scanner:
                tt_id = item.get("id")
                if isinstance(tt_id, int):
                    return tt_id
        raise ConfigError(
            f"Test type {opts.scanner!r} not found in DefectDojo",
            hint="Check the scanner name against `dd test-types list`.",
        )

    def _update_engagement_build_metadata(self, engagement_id: int) -> None:
        opts = self._opts
        if opts.build_id is None and opts.commit_hash is None and opts.branch_tag is None:
            return
        payload = {
            "build_id": opts.build_id,
            "commit_hash": opts.commit_hash,
            "branch_tag": opts.branch_tag,
        }
        self._client.patch(f"/api/v2/engagements/{engagement_id}/", json=payload)

    # ------------------------------------------------------------------ #
    #  Auto-create workflow                                              #
    # ------------------------------------------------------------------ #

    def _run_auto_create(self) -> dict[str, Any]:
        return self._reimport(test_id=None, auto_create=True)

    # ------------------------------------------------------------------ #
    #  Shared upload                                                     #
    # ------------------------------------------------------------------ #

    def _reimport(
        self,
        *,
        test_id: int | None,
        auto_create: bool = False,
    ) -> dict[str, Any]:
        opts = self._opts
        payload: dict[str, Any] = {
            "scan_date": _today_iso(),
            "scan_type": opts.scanner,
            "active": opts.active,
            "verified": opts.verified,
            "push_to_jira": opts.push_to_jira,
            "close_old_findings": opts.close_old_findings,
            "close_old_findings_product_scope": opts.close_old_findings_product_scope,
            "do_not_reactivate": opts.do_not_reactivate,
        }

        if test_id is not None:
            payload["test"] = test_id

        if auto_create:
            payload["auto_create_context"] = True
            payload["product_type_name"] = opts.product_type_name
            payload["product_name"] = opts.product_name
            if opts.engagement_name is not None:
                payload["engagement_name"] = opts.engagement_name
            if opts.test_name is not None:
                payload["test_title"] = opts.test_name
            if opts.deduplication_on_engagement:
                payload["deduplication_on_engagement"] = True
            if opts.product_description is not None:
                payload["product_description"] = opts.product_description
            if opts.product_business_criticality is not None:
                payload["business_criticality"] = opts.product_business_criticality
            if opts.product_platform is not None:
                payload["platform"] = opts.product_platform
            if opts.product_lifecycle is not None:
                payload["lifecycle"] = opts.product_lifecycle
            if opts.product_origin is not None:
                payload["origin"] = opts.product_origin
            if opts.product_external_audience:
                payload["external_audience"] = True
            if opts.product_internet_accessible:
                payload["internet_accessible"] = True
            if opts.engagement_target_end != "2999-12-31":
                payload["engagement_end_date"] = opts.engagement_target_end
            if opts.engagement_description is not None:
                payload["engagement_description"] = opts.engagement_description
            if opts.engagement_version is not None:
                payload["engagement_version"] = opts.engagement_version
            if opts.apply_tags_to_findings:
                payload["apply_tags_to_findings"] = True
            if opts.apply_tags_to_endpoints:
                payload["apply_tags_to_endpoints"] = True
            if not opts.create_finding_groups_for_all_findings:
                payload["create_finding_groups_for_all_findings"] = False

        # Optional fields shared by both modes
        if opts.minimum_severity is not None:
            payload["minimum_severity"] = opts.minimum_severity
        if opts.group_by is not None:
            payload["group_by"] = opts.group_by
        if opts.version is not None:
            payload["version"] = opts.version
        if opts.endpoint_id is not None:
            payload["endpoint_to_add"] = opts.endpoint_id
        if opts.service is not None:
            payload["service"] = opts.service
        if opts.api_scan_configuration_id is not None:
            payload["api_scan_configuration"] = opts.api_scan_configuration_id
        if opts.source_code_management_uri is not None:
            payload["source_code_management_uri"] = opts.source_code_management_uri
        if auto_create:
            # Auto-create-only optional fields
            if opts.build_id is not None:
                payload["build_id"] = opts.build_id
            if opts.commit_hash is not None:
                payload["commit_hash"] = opts.commit_hash
            if opts.branch_tag is not None:
                payload["branch_tag"] = opts.branch_tag
            if opts.lead is not None:
                payload["lead"] = opts.lead
            if opts.test_environment_name is not None:
                payload["environment"] = opts.test_environment_name

        file_arg: tuple[str, bytes] | None = None
        if opts.file is not None:
            path = Path(opts.file)
            if not path.exists():
                raise ValidationError(f"Scan file not found: {path}")
            file_arg = (path.name, path.read_bytes())

        return self._client.upload(
            "/api/v2/reimport-scan/",
            data=payload,
            file=file_arg,
        )


def make_options_from_kwargs(**overrides: Any) -> ImportFindingsOptions:
    """Build an `ImportFindingsOptions` from explicit kwargs, ignoring None.

    Used by the CLI command to merge user-supplied flags on top of values
    pydantic-settings already pulled from the env. Without this helper, a
    None CLI value would clobber the env-derived value.
    """
    base: Mapping[str, Any] = ImportFindingsOptions().model_dump(exclude_none=False)
    merged = {**base}
    for key, value in overrides.items():
        if value is not None:
            merged[key] = value
    return ImportFindingsOptions.model_validate(merged)


# Re-export for type-checkers
__all__ = [
    "VALID_BUSINESS_CRITICALITIES",
    "VALID_LIFECYCLES",
    "VALID_PLATFORMS",
    "ImportFindingsOptions",
    "ImportFindingsWorkflow",
    "make_options_from_kwargs",
]


# Suppress pydantic ConfigDict / SettingsConfigDict mypy warning when both are imported.
_ = ConfigDict
