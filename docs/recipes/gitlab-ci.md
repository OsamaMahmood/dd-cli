# GitLab CI

## Minimal pipeline

```yaml
variables:
  DD_PRODUCT_TYPE_NAME: "GitLab Projects"
  DD_PRODUCT_NAME: "$CI_PROJECT_PATH"
  DD_ENGAGEMENT_NAME: "$CI_COMMIT_REF_SLUG"
  DD_AUTO_CREATE_CONTEXT: "true"
  # DD_URL and DD_API_KEY are set as protected/masked GitLab variables.

stages:
  - test
  - upload

trivy:
  stage: test
  image: aquasec/trivy:latest
  script:
    - trivy fs --format json -o trivy.json .
  artifacts:
    paths: [trivy.json]
    expire_in: 1 day

upload_trivy:
  stage: upload
  image: ghcr.io/osamamahmood/dd-cli:2
  needs: [trivy]
  variables:
    DD_TEST_NAME: "Trivy"
    DD_TEST_TYPE_NAME: "Trivy Scan"
    DD_FILE_NAME: "trivy.json"
  script:
    - dd-reimport-findings
```

## Multi-scanner pipeline

```yaml
variables:
  DD_PRODUCT_TYPE_NAME: "GitLab Projects"
  DD_PRODUCT_NAME: "$CI_PROJECT_PATH"
  DD_ENGAGEMENT_NAME: "$CI_COMMIT_REF_SLUG"
  DD_BUILD_ID: "$CI_PIPELINE_ID"
  DD_COMMIT_HASH: "$CI_COMMIT_SHA"
  DD_BRANCH_TAG: "$CI_COMMIT_REF_NAME"
  DD_AUTO_CREATE_CONTEXT: "true"

.dd_upload: &dd_upload
  stage: upload
  image: ghcr.io/osamamahmood/dd-cli:2
  script: [dd-reimport-findings]

stages:
  - scan
  - upload

trivy:
  stage: scan
  image: aquasec/trivy:latest
  script: [trivy fs --format json -o trivy.json .]
  artifacts:
    paths: [trivy.json]
    expire_in: 1 day

bandit:
  stage: scan
  image: python:3.12-slim
  before_script: [pip install bandit]
  script: [bandit -r src/ -f json -o bandit.json || true]
  artifacts:
    paths: [bandit.json]
    expire_in: 1 day

cloc:
  stage: scan
  image: node:20-alpine
  before_script: [npm install -g cloc]
  script: [cloc src --json --out cloc.json]
  artifacts:
    paths: [cloc.json]
    expire_in: 1 day

upload_trivy:
  <<: *dd_upload
  needs: [trivy]
  variables:
    DD_TEST_NAME: "Trivy"
    DD_TEST_TYPE_NAME: "Trivy Scan"
    DD_FILE_NAME: "trivy.json"

upload_bandit:
  <<: *dd_upload
  needs: [bandit]
  variables:
    DD_TEST_NAME: "Bandit"
    DD_TEST_TYPE_NAME: "Bandit Scan"
    DD_FILE_NAME: "bandit.json"

upload_cloc:
  <<: *dd_upload
  needs: [cloc]
  variables:
    DD_FILE_NAME: "cloc.json"
  script: [dd-import-languages]    # different shim
```

## Notes

- **Image pinning.** Pin to a major version (`:2`) so dependabot bumps catch patches and minors but not breaking changes.
- **Secrets.** Set `DD_URL` and `DD_API_KEY` at the project or group level as protected, masked CI/CD variables.
- **Per-stage env.** GitLab merges `.dd_upload` template variables with per-job `variables:`, so the per-job block only needs the scanner-specific bits.
- **GitLab Runner registries.** If your runner caches Docker images, the `dd-cli` image pull will be near-instant after the first run.

## Branching on typed exit codes

`dd-reimport-findings` flattens errors to exit 1 (legacy contract). For typed exit codes, use the new command:

```yaml
upload_trivy:
  stage: upload
  image: ghcr.io/osamamahmood/dd-cli:2
  needs: [trivy]
  script:
    - |
      set +e
      dd import findings \
        --file trivy.json \
        --scanner "Trivy Scan" \
        --product-type "$DD_PRODUCT_TYPE_NAME" \
        --product "$DD_PRODUCT_NAME" \
        --auto-create --yes
      rc=$?
      set -e
      case $rc in
        0) echo "ok";;
        3) echo "auth failed — rotate DD_API_KEY"; exit 1;;
        8) echo "network blip"; exit $rc;;
        *) echo "upload failed: $rc"; exit $rc;;
      esac
```

See [migration](../migration.md#exit-code-contract) for the full code map.
