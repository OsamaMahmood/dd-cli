"""Mock DefectDojo data for `dd report generate --sample`.

Each function mirrors the shape a real DefectDojo API call would
return, so the renderer exercises every branch (all severities,
zero-finding tests, KEV badges, optional fields, etc.) without
contacting an actual server.
"""

from __future__ import annotations

from typing import Any


def sample_product() -> dict[str, Any]:
    return {
        "id": 9999,
        "name": "sample-app",
        "description": (
            "A demo product used to preview the report layout. "
            "This text is rendered exactly as it would be from a real "
            "DefectDojo product description field."
        ),
        "business_criticality": "high",
        "platform": "web",
        "lifecycle": "production",
        "prod_numeric_grade": 78,
        "tags": ["demo", "sample"],
    }


def sample_engagements() -> list[dict[str, Any]]:
    return [
        {
            "id": 7001,
            "name": "Q2 Pre-release Scan",
            "description": "Pre-release security review for the Q2 release branch.",
            "status": "In Progress",
            "active": True,
            "version": "2.4.0",
            "target_start": "2026-04-01",
            "target_end": "2026-04-30",
            "branch_tag": "release/2.4",
            "commit_hash": "a1b2c3d4e5f6",
            "build_id": "ci-1842",
            "engagement_type": "CI/CD",
        },
        {
            "id": 7002,
            "name": "Continuous Monitoring",
            "description": "Daily automated scans on the main branch.",
            "status": "In Progress",
            "active": True,
            "version": "main",
            "target_start": "2026-01-01",
            "target_end": "2026-12-31",
            "branch_tag": "main",
            "commit_hash": "9f8e7d6c5b4a",
            "build_id": "ci-1843",
            "engagement_type": "CI/CD",
        },
    ]


def sample_tests_by_engagement() -> dict[int, list[dict[str, Any]]]:
    return {
        7001: [
            {
                "id": 8001,
                "title": "",
                "scan_type": "SAST Scan",
                "test_type": 101,
                "test_type_name": "SAST Scan",
                "target_start": "2026-04-15T09:00:00Z",
                "target_end": "2026-04-15T09:42:00Z",
                "branch_tag": "release/2.4",
                "commit_hash": "a1b2c3d4e5f6",
                "build_id": "ci-1842",
                "version": "2.4.0",
                "engagement": 7001,
            },
            {
                "id": 8002,
                "title": "",
                "scan_type": "IAC Scan",
                "test_type": 102,
                "test_type_name": "IAC Scan",
                "target_start": "2026-04-15T09:45:00Z",
                "target_end": "2026-04-15T09:51:00Z",
                "branch_tag": "release/2.4",
                "commit_hash": "a1b2c3d4e5f6",
                "build_id": "ci-1842",
                "version": "2.4.0",
                "engagement": 7001,
            },
            {
                "id": 8003,
                "title": "",
                "scan_type": "Secret Scan",
                "test_type": 103,
                "test_type_name": "Secret Scan",
                "target_start": "2026-04-15T09:55:00Z",
                "target_end": "2026-04-15T09:58:00Z",
                "branch_tag": "release/2.4",
                "commit_hash": "a1b2c3d4e5f6",
                "build_id": "ci-1842",
                "version": "2.4.0",
                "engagement": 7001,
            },
        ],
        7002: [
            {
                "id": 8004,
                "title": "",
                "scan_type": "DAST Scan",
                "test_type": 104,
                "test_type_name": "DAST Scan",
                "target_start": "2026-04-27T03:00:00Z",
                "target_end": "2026-04-27T03:31:00Z",
                "branch_tag": "main",
                "commit_hash": "9f8e7d6c5b4a",
                "build_id": "ci-1843",
                "version": "main",
                "engagement": 7002,
            },
            {
                "id": 8005,
                "title": "",
                "scan_type": "Dependency Scan",
                "test_type": 105,
                "test_type_name": "Dependency Scan",
                "target_start": "2026-04-27T03:35:00Z",
                "target_end": "2026-04-27T03:37:00Z",
                "branch_tag": "main",
                "commit_hash": "9f8e7d6c5b4a",
                "build_id": "ci-1843",
                "version": "main",
                "engagement": 7002,
            },
            {
                "id": 8006,
                "title": "",
                "scan_type": "Container Scan",
                "test_type": 106,
                "test_type_name": "Container Scan",
                "target_start": "2026-04-27T03:40:00Z",
                "target_end": "2026-04-27T03:48:00Z",
                "branch_tag": "main",
                "commit_hash": "9f8e7d6c5b4a",
                "build_id": "ci-1843",
                "version": "main",
                "engagement": 7002,
            },
        ],
    }


def sample_findings_by_test() -> dict[int, list[dict[str, Any]]]:
    return {
        # SAST: critical + high + medium
        8001: [
            {
                "id": 90001,
                "title": "SQL injection in user search endpoint",
                "severity": "Critical",
                "numerical_severity": "S0",
                "cwe": 89,
                "cve": "",
                "cvssv3_score": 9.8,
                "description": (
                    "User-supplied input is concatenated directly into a SQL query in the "
                    "`/api/users/search` endpoint. An attacker can inject arbitrary SQL and "
                    "exfiltrate data from the `users` and `sessions` tables.\n\n"
                    "The vulnerable code path:\n\n"
                    "```python\n"
                    "def search_users(query):\n"
                    "    sql = f\"SELECT * FROM users WHERE name LIKE '%{query}%'\"\n"
                    "    return db.execute(sql)\n"
                    "```\n"
                ),
                "impact": "**Full database read**, possible write, credential theft.",
                "steps_to_reproduce": (
                    "1. Send: `GET /api/users/search?q=' OR 1=1 --`\n"
                    "2. Observe full user table returned in the response.\n"
                    "3. Iterate to extract `sessions` and `password_hashes`."
                ),
                "mitigation": (
                    "- Use parameterized queries (the project's ORM helper).\n"
                    "- Add a regression test that asserts the query is parameterized.\n"
                    "- Apply input validation at the request boundary."
                ),
                "references": (
                    "- [OWASP A03 — Injection](https://owasp.org/Top10/A03_2021-Injection/)\n"
                    "- [CWE-89](https://cwe.mitre.org/data/definitions/89.html)"
                ),
                "file_path": "app/handlers/users.py",
                "line": 142,
                "component_name": "users-api",
                "component_version": "2.4.0",
                "date": "2026-04-15",
                "static_finding": True,
                "dynamic_finding": False,
                "tags": ["sast", "injection", "owasp-a03"],
                "age": 14,
                "sla_days_remaining": -2,
                "sla_expiration_date": "2026-04-27",
                "epss_score": 0.9421,
                "epss_percentile": 0.998,
                "known_exploited": True,
                "kev_date": "2024-08-12",
                "cvssv4_score": 9.3,
                "fix_available": True,
                "fix_version": "2.4.1",
                "planned_remediation_date": "2026-05-05",
                "planned_remediation_version": "2.4.1",
                "effort_for_fixing": "Low",
                "severity_justification": (
                    "Confirmed exploitable on staging. Public CVE with active exploitation in the wild."
                ),
                "scanner_confidence": 95,
                "last_reviewed": "2026-04-26",
                "service": "users-api",
                "sast_source_file_path": "app/handlers/users.py",
                "sast_source_line": 142,
                "sast_source_object": "search_users(query)",
                "sast_sink_object": "db.execute(raw_sql)",
                "endpoints": [501, 502, 503],
            },
            {
                "id": 90002,
                "title": "Hardcoded JWT signing key",
                "severity": "High",
                "numerical_severity": "S1",
                "cwe": 798,
                "cve": "",
                "cvssv3_score": 7.5,
                "description": (
                    "A JWT signing key is hardcoded as a module-level constant. "
                    "Anyone with read access to the repo can forge valid tokens."
                ),
                "impact": "Authentication bypass for any user.",
                "steps_to_reproduce": "",
                "mitigation": "Move the key to the secrets manager and rotate it.",
                "references": "",
                "file_path": "app/auth/jwt.py",
                "line": 12,
                "component_name": "auth",
                "component_version": "2.4.0",
                "date": "2026-04-15",
                "static_finding": True,
                "dynamic_finding": False,
                "tags": ["sast", "secret"],
                "age": 14,
                "sla_days_remaining": 16,
                "sla_expiration_date": "2026-05-15",
                "epss_score": 0.0832,
                "epss_percentile": 0.812,
                "known_exploited": False,
                "cvssv4_score": 8.2,
                "fix_available": False,
                "planned_remediation_date": "2026-05-10",
                "effort_for_fixing": "Medium",
                "scanner_confidence": 80,
                "last_reviewed": "2026-04-20",
                "sast_source_file_path": "app/auth/jwt.py",
                "sast_source_line": 12,
                "sast_source_object": "JWT_SECRET",
                "endpoints": [],
            },
            {
                "id": 90003,
                "title": "Insecure use of MD5 for password hashing",
                "severity": "Medium",
                "numerical_severity": "S2",
                "cwe": 327,
                "cve": "",
                "cvssv3_score": 5.3,
                "description": "Password verification path falls back to MD5 hashes.",
                "impact": "Faster offline cracking if the user table is leaked.",
                "steps_to_reproduce": "",
                "mitigation": "Migrate remaining MD5 hashes to argon2id on next login.",
                "references": "",
                "file_path": "app/auth/legacy.py",
                "line": 47,
                "component_name": "auth",
                "component_version": "2.4.0",
                "date": "2026-04-15",
                "static_finding": True,
                "dynamic_finding": False,
                "tags": ["sast", "crypto"],
                "age": 14,
                "sla_days_remaining": 76,
                "sla_expiration_date": "2026-07-14",
                "epss_score": 0.0021,
                "epss_percentile": 0.231,
                "known_exploited": False,
                "fix_available": False,
                "effort_for_fixing": "High",
                "scanner_confidence": 60,
                "endpoints": [],
            },
        ],
        # IAC: high + low
        8002: [
            {
                "id": 90004,
                "title": "S3 bucket allows public read",
                "severity": "High",
                "numerical_severity": "S1",
                "cwe": 732,
                "cve": "",
                "cvssv3_score": 7.2,
                "description": 'Terraform module sets acl = "public-read" on a bucket holding user uploads.',
                "impact": "Any user file is readable by anyone on the internet.",
                "steps_to_reproduce": "",
                "mitigation": 'Set acl = "private" and serve via signed URLs.',
                "references": "",
                "file_path": "infra/storage.tf",
                "line": 33,
                "component_name": "infra",
                "component_version": "",
                "date": "2026-04-15",
                "static_finding": True,
                "dynamic_finding": False,
                "tags": ["iac", "terraform", "aws"],
                "age": 14,
                "sla_days_remaining": 1,
                "sla_expiration_date": "2026-04-30",
                "epss_score": None,
                "epss_percentile": None,
                "known_exploited": False,
                "fix_available": True,
                "fix_version": "main",
                "effort_for_fixing": "Low",
                "scanner_confidence": 100,
                "last_reviewed": "2026-04-22",
                "endpoints": [],
            },
            {
                "id": 90005,
                "title": "Security group allows 0.0.0.0/0 on SSH",
                "severity": "Low",
                "numerical_severity": "S3",
                "cwe": 284,
                "cve": "",
                "cvssv3_score": 3.7,
                "description": "Bastion SG opens port 22 to the world.",
                "impact": "Increased brute-force surface area.",
                "steps_to_reproduce": "",
                "mitigation": "Restrict to the office VPN CIDR.",
                "references": "",
                "file_path": "infra/network.tf",
                "line": 88,
                "component_name": "infra",
                "component_version": "",
                "date": "2026-04-15",
                "static_finding": True,
                "dynamic_finding": False,
                "tags": ["iac", "terraform"],
                "age": 14,
                "sla_days_remaining": 256,
                "sla_expiration_date": "2027-01-10",
                "epss_score": 0.0008,
                "epss_percentile": 0.131,
                "known_exploited": False,
                "fix_available": True,
                "effort_for_fixing": "Low",
                "scanner_confidence": 90,
                "endpoints": [],
            },
        ],
        # Secret Scan: zero findings — exercises the empty-test branch
        8003: [],
        # DAST: info
        8004: [
            {
                "id": 90006,
                "title": "Server header exposes nginx version",
                "severity": "Info",
                "numerical_severity": "S4",
                "cwe": 200,
                "cve": "",
                "cvssv3_score": 0.0,
                "description": "All responses include `Server: nginx/1.21.6`.",
                "impact": "Minor information disclosure that aids fingerprinting.",
                "steps_to_reproduce": "curl -I https://app.example.com/",
                "mitigation": "Set `server_tokens off` in nginx.conf.",
                "references": "",
                "file_path": "",
                "line": None,
                "component_name": "",
                "component_version": "",
                "date": "2026-04-27",
                "static_finding": False,
                "dynamic_finding": True,
                "tags": ["dast"],
                "age": 2,
                "sla_days_remaining": None,
                "sla_expiration_date": None,
                "epss_score": None,
                "epss_percentile": None,
                "known_exploited": False,
                "fix_available": True,
                "effort_for_fixing": "Low",
                "scanner_confidence": 100,
                "service": "edge-nginx",
                "url": "https://app.example.com/",
                "param": "",
                "payload": "",
                "endpoints": [501],
            },
        ],
        # Dependency: high CVE
        8005: [
            {
                "id": 90007,
                "title": "lodash <4.17.21 — prototype pollution",
                "severity": "High",
                "numerical_severity": "S1",
                "cwe": 1321,
                "cve": "CVE-2021-23337",
                "cvssv3_score": 7.2,
                "description": "Lodash versions before 4.17.21 are vulnerable to command injection via template.",
                "impact": "RCE in code paths that compile lodash templates from untrusted input.",
                "steps_to_reproduce": "",
                "mitigation": "Bump lodash to ^4.17.21.",
                "references": "https://nvd.nist.gov/vuln/detail/CVE-2021-23337",
                "file_path": "package-lock.json",
                "line": None,
                "component_name": "lodash",
                "component_version": "4.17.20",
                "date": "2026-04-27",
                "static_finding": True,
                "dynamic_finding": False,
                "tags": ["sca", "npm"],
                "age": 2,
                "sla_days_remaining": 28,
                "sla_expiration_date": "2026-05-27",
                "epss_score": 0.4218,
                "epss_percentile": 0.974,
                "known_exploited": False,
                "cvssv4_score": 7.8,
                "fix_available": True,
                "fix_version": "4.17.21",
                "planned_remediation_date": "2026-05-02",
                "planned_remediation_version": "4.17.21",
                "effort_for_fixing": "Low",
                "scanner_confidence": 100,
                "endpoints": [],
            },
        ],
        # Container Scan: zero findings — second empty case
        8006: [],
    }


def sample_test_type_names() -> dict[int, str]:
    return {
        101: "SAST Scan",
        102: "IAC Scan",
        103: "Secret Scan",
        104: "DAST Scan",
        105: "Dependency Scan",
        106: "Container Scan",
    }


def sample_sla_configurations() -> list[dict[str, Any]]:
    return [
        {
            "id": 1,
            "name": "Default SLA",
            "critical": 7,
            "high": 30,
            "medium": 90,
            "low": 365,
        }
    ]


def sample_risk_acceptances() -> list[dict[str, Any]]:
    """One risk acceptance covering finding 90003 (MD5)."""
    return [
        {
            "id": 5001,
            "name": "Legacy MD5 deferral — Q2",
            "decision": "Accept",
            "decision_details": (
                "Migration to argon2id is **scheduled** for Q3. We have compensating "
                "controls: rate limiting on login, alerting on credential-stuffing patterns, "
                "and forced rotation on next login."
            ),
            "recommendation": "Mitigate",
            "accepted_by": "Jane Smith (CISO)",
            "expiration_date": "2026-09-30",
            "expiration_date_handled": None,
            "created": "2026-04-20",
            "accepted_findings": [90003],
        }
    ]


def sample_notes_by_finding() -> dict[int, list[dict[str, Any]]]:
    return {
        90001: [
            {
                "id": 1,
                "author": {"username": "alice"},
                "date": "2026-04-26",
                "entry": (
                    "Confirmed exploitable on staging. Patch in `release/2.4.1` blocks "
                    "the vector — verifying tomorrow."
                ),
                "private": False,
            },
            {
                "id": 2,
                "author": {"username": "bob"},
                "date": "2026-04-27",
                "entry": "Customer SOC also flagged this — keeping at Critical.",
                "private": True,
            },
        ],
        90004: [
            {
                "id": 3,
                "author": {"username": "alice"},
                "date": "2026-04-22",
                "entry": "Cleared change ticket. Awaiting Terraform PR review.",
                "private": False,
            },
        ],
    }


def sample_jira_by_finding() -> dict[int, list[dict[str, Any]]]:
    return {
        90001: [
            {
                "id": 1,
                "jira_id": "12345",
                "jira_key": "SEC-1138",
                "jira_creation": "2026-04-15",
                "jira_change": "2026-04-27",
                "url": "https://jira.example.com/browse/SEC-1138",
            }
        ],
        90007: [
            {
                "id": 2,
                "jira_id": "12346",
                "jira_key": "SEC-1141",
                "jira_creation": "2026-04-27",
                "jira_change": "2026-04-27",
                "url": "https://jira.example.com/browse/SEC-1141",
            }
        ],
    }


def sample_test_imports_by_test() -> dict[int, list[dict[str, Any]]]:
    """Mock scan deltas — varied so each test shows different activity."""
    return {
        8001: [
            {
                "id": 1,
                "created": "2026-04-15T09:00:00Z",
                "build_id": "ci-1842",
                "branch_tag": "release/2.4",
                "commit_hash": "a1b2c3d4e5f6",
                "test_import_finding_action_set": [
                    {"action": "created"},
                    {"action": "created"},
                    {"action": "reactivated"},
                    {"action": "closed"},
                    {"action": "untouched"},
                ],
            },
            {
                "id": 0,
                "created": "2026-04-08T09:00:00Z",
                "build_id": "ci-1801",
                "branch_tag": "release/2.4",
                "test_import_finding_action_set": [],
            },
        ],
        8002: [
            {
                "id": 2,
                "created": "2026-04-15T09:45:00Z",
                "build_id": "ci-1842",
                "branch_tag": "release/2.4",
                "commit_hash": "a1b2c3d4e5f6",
                "test_import_finding_action_set": [
                    {"action": "created"},
                    {"action": "untouched"},
                ],
            },
        ],
        8003: [
            {
                "id": 3,
                "created": "2026-04-15T09:55:00Z",
                "build_id": "ci-1842",
                "branch_tag": "release/2.4",
                "commit_hash": "a1b2c3d4e5f6",
                "test_import_finding_action_set": [
                    {"action": "closed"},
                    {"action": "closed"},
                ],
            },
        ],
        8004: [
            {
                "id": 4,
                "created": "2026-04-27T03:00:00Z",
                "build_id": "ci-1843",
                "branch_tag": "main",
                "commit_hash": "9f8e7d6c5b4a",
                "test_import_finding_action_set": [
                    {"action": "created"},
                    {"action": "untouched"},
                    {"action": "untouched"},
                ],
            },
        ],
        8005: [
            {
                "id": 5,
                "created": "2026-04-27T03:35:00Z",
                "build_id": "ci-1843",
                "branch_tag": "main",
                "commit_hash": "9f8e7d6c5b4a",
                "test_import_finding_action_set": [
                    {"action": "created"},
                    {"action": "closed"},
                    {"action": "closed"},
                    {"action": "untouched"},
                    {"action": "untouched"},
                ],
            },
        ],
        8006: [
            {
                "id": 6,
                "created": "2026-04-27T03:40:00Z",
                "build_id": "ci-1843",
                "branch_tag": "main",
                "test_import_finding_action_set": [
                    {"action": "untouched"},
                    {"action": "untouched"},
                ],
            },
        ],
    }
