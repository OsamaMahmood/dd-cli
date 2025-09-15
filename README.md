# dd-import

*This is a continuation and enhancement of the original dd-import project.*

> A utility to (re-)import findings and language data into [DefectDojo](https://www.defectdojo.org/)

Findings and languages can be imported into DefectDojo via an [API](https://defectdojo.github.io/django-DefectDojo/integrations/api-v2-docs/). To make automated build and deploy pipelines easier to implement, `dd-import` provides some convenience functions:

- Product types, products, engagements and tests will be created if they are not existing. This avoids manual preparation in DefectDojo or complicated steps within the pipeline.
- Product types, products, engagements and tests are referenced by name. This make pipelines more readable than using IDs.
- Build information for `build_id`, `commit_hash` and `branch_tag` can be updated when uploading findings.
- No need to deal with `curl` and its syntax within the pipeline. This makes pipelines shorter and better readable.
- All parameters are provided via environment variables, which works well with pipeline definitions like GitHub Actions or GitLab CI.

## User guide

### Installation and commands

**Python**

`dd-import` can be installed with pip. Only Python 3.8 and up is supported.

```bash
pip install dd-import
```

The command `dd-reimport-findings` re-imports findings into DefectDojo. Even though the name suggests otherwise, you do not need to do an initial import first.

The command `dd-import-languages` imports languages data that have been gathered with the tool [cloc](https://github.com/AlDanial/cloc), see [Languages and lines of code](https://defectdojo.github.io/django-DefectDojo/integrations/languages/) for more details.


**Docker**

Docker images can be found in the releases section of this repository.

A re-import of findings can be started with

```bash
docker run --rm dd-import:latest dd-reimport-findings.sh
```

Importing languages data can be started with


```bash
docker run --rm dd-import:latest dd-import-languages.sh
```

Please note you have to set the environment variables as described below and mount a folder containing the file with scan results when running the docker container.

`/usr/local/dd-import` is the working directory of the docker image, all commands are located in the `/usr/local/dd-import/bin` folder.

### Parameters

All parameters need to be provided as environment variables:

## 🚀 Enhanced Features (NEW!)

**Auto-Create Workflow**: Set `DD_AUTO_CREATE_CONTEXT=true` to enable one-call workflow that automatically creates all resources!

**Rich Metadata**: Add business context with criticality levels, platforms, lifecycle stages, and comprehensive tagging.

**Smart Workflow Selection**: Automatically chooses between traditional multi-call workflow and new auto-create workflow.

## Environment Variables

### Core Parameters (Required)

| Parameter                           | Re-import findings | Import languages | Remark                                                                                            |
|-------------------------------------|:------------------:|:----------------:|---------------------------------------------------------------------------------------------------|
| DD_URL                              | Mandatory          | Mandatory        | Base URL of the DefectDojo instance                                                               |
| DD_API_KEY                          | Mandatory          | Mandatory        | Shall be defined as a secret, eg. a protected variable in GitLab or an encrypted secret in GitHub |
| DD_PRODUCT_TYPE_NAME                | Mandatory          | Mandatory        | If a product type with this name does not exist, it will be created                               |
| DD_PRODUCT_NAME                     | Mandatory          | Mandatory        | If a product with this name does not exist, it will be created                                    |
| DD_ENGAGEMENT_NAME                  | Mandatory          | -                | If an engagement with this name does not exist for the given product, it will be created          |
| DD_ENGAGEMENT_TARGET_START          | Optional           | -                | Format: YYYY-MM-DD, default: `today`. The target start date for a newly created engagement.       |
| DD_ENGAGEMENT_TARGET_END            | Optional           | -                | Format: YYYY-MM-DD, default: `2999-12-31`. The target start date for a newly created engagement.  |
| DD_TEST_NAME                        | Mandatory          | -                | If a test with this name does not exist for the given engagement, it will be created              |
| DD_TEST_TYPE_NAME                   | Mandatory          | -                | From DefectDojo's list of test types, eg. `Trivy Scan`                                            |
| DD_FILE_NAME                        | Optional           | Mandatory        |                                                                                                   |
| DD_ACTIVE                           | Optional           | -                | Default: `true`                                                                                   |
| DD_VERIFIED                         | Optional           | -                | Default: `true`                                                                                   |
| DD_MINIMUM_SEVERITY                 | Optional           | -                |                                                                                                   |
| DD_GROUP_BY                         | Optional           | -                | Group by file path, component name, component name + version                                      |
| DD_PUSH_TO_JIRA                     | Optional           | -                | Default: `false`                                                                                  |
| DD_CLOSE_OLD_FINDINGS               | Optional           | -                | Default: `true`                                                                                   |
| DD_CLOSE_OLD_FINDINGS_PRODUCT_SCOPE | Optional           | -                | Default: `false`                                                                                  |
| DD_DO_NOT_REACTIVATE                | Optional           | -                | Default: `false`                                                                                  |
| DD_VERSION                          | Optional           | -                |                                                                                                   |
| DD_ENDPOINT_ID                      | Optional           | -                |                                                                                                   |
| DD_SERVICE                          | Optional           | -                |                                                                                                   |
| DD_BUILD_ID                         | Optional           | -                |                                                                                                   |
| DD_COMMIT_HASH                      | Optional           | -                |                                                                                                   |
| DD_BRANCH_TAG                       | Optional           | -                |                                                                                                   |
| DD_API_SCAN_CONFIGURATION_ID        | Optional           | -                | Id of the API scan configuration for API based parsers, e.g. SonarQube                            |
| DD_SOURCE_CODE_MANAGEMENT_URI       | Optional           | -                |                                                                                                   |
| DD_SSL_VERIFY                       | Optional           | Optional         | Disable SSL verification by setting to `false` or `0`. Default: `true`                            |
| DD_EXTRA_HEADER_1         | Optional           | Optional         | If extra header key is needed for auth in wafs or similar |
| DD_EXTRA_HEADER_1_VALUE   | Optional           | Optional         | The corresponding value for extra header key |
| DD_EXTRA_HEADER_2         | Optional           | Optional         | If extra header key is needed for auth in wafs or similar |
| DD_EXTRA_HEADER_2_VALUE   | Optional           | Optional         | The corresponding value for extra header key |

### 🚀 Enhanced Auto-Create Parameters (NEW!)

| Parameter                           | Re-import findings | Import languages | Remark                                                                                            |
|-------------------------------------|:------------------:|:----------------:|---------------------------------------------------------------------------------------------------|
| DD_AUTO_CREATE_CONTEXT              | Optional           | -                | **GAME CHANGER!** `true` = Single API call creates all resources. `false` = Traditional workflow (default) |
| DD_DEDUPLICATION_ON_ENGAGEMENT      | Optional           | -                | `true` = Scope finding deduplication to engagement level. Default: `false`                       |

### 📊 Enhanced Product Metadata (NEW!)

| Parameter                           | Re-import findings | Import languages | Remark                                                                                            |
|-------------------------------------|:------------------:|:----------------:|---------------------------------------------------------------------------------------------------|
| DD_PRODUCT_DESCRIPTION              | Optional           | Optional         | Detailed product description (falls back to product name)                                        |
| DD_PRODUCT_BUSINESS_CRITICALITY     | Optional           | Optional         | `very high`, `high`, `medium`, `low`, `very low`, `none`                                          |
| DD_PRODUCT_PLATFORM                 | Optional           | Optional         | `web service`, `desktop`, `iot`, `mobile`, `web`                                                  |
| DD_PRODUCT_LIFECYCLE                | Optional           | Optional         | `construction`, `production`, `retirement`                                                        |
| DD_PRODUCT_ORIGIN                   | Optional           | Optional         | `third party library`, `purchased`, `contractor`, `internal`, `open source`, `outsourced`        |
| DD_PRODUCT_INTERNET_ACCESSIBLE      | Optional           | Optional         | `true`/`false` - Is the product internet accessible?                                             |
| DD_PRODUCT_EXTERNAL_AUDIENCE        | Optional           | Optional         | `true`/`false` - Does the product have external users?                                           |
| DD_PRODUCT_TAGS                     | Optional           | Optional         | Comma-separated tags, e.g., `security,webapp,critical`                                           |

### 🎯 Enhanced Engagement Metadata (NEW!)

| Parameter                           | Re-import findings | Import languages | Remark                                                                                            |
|-------------------------------------|:------------------:|:----------------:|---------------------------------------------------------------------------------------------------|
| DD_ENGAGEMENT_DESCRIPTION           | Optional           | -                | Detailed engagement description                                                                   |
| DD_ENGAGEMENT_VERSION               | Optional           | -                | Version of the product being tested                                                               |
| DD_ENGAGEMENT_STATUS                | Optional           | -                | `Not Started`, `Blocked`, `Cancelled`, `Completed`, `In Progress` (default), `On Hold`, `Waiting for Resource` |
| DD_ENGAGEMENT_THREAT_MODEL          | Optional           | -                | `true`/`false` - Include threat modeling activities                                              |
| DD_ENGAGEMENT_API_TEST              | Optional           | -                | `true`/`false` - Include API testing                                                             |
| DD_ENGAGEMENT_PEN_TEST              | Optional           | -                | `true`/`false` - Include penetration testing                                                     |
| DD_ENGAGEMENT_TAGS                  | Optional           | -                | Comma-separated engagement tags                                                                   |

### ⚙️ Enhanced Finding Controls (NEW!)

| Parameter                               | Re-import findings | Import languages | Remark                                                                                        |
|-----------------------------------------|:------------------:|:----------------:|-----------------------------------------------------------------------------------------------|
| DD_APPLY_TAGS_TO_FINDINGS               | Optional           | -                | `true`/`false` - Apply tags to imported findings                                             |
| DD_APPLY_TAGS_TO_ENDPOINTS              | Optional           | -                | `true`/`false` - Apply tags to endpoints                                                     |
| DD_CREATE_FINDING_GROUPS_FOR_ALL_FINDINGS | Optional        | -                | `true` (default)/`false` - Create finding groups even for single findings                    |
| DD_FINDING_TAGS                         | Optional           | -                | Comma-separated tags to apply to findings, e.g., `automated,security,scan`                  |

### Usage Examples

#### 🚀 NEW: Auto-Create Workflow (Recommended)

The enhanced auto-create workflow simplifies integration by handling all resource creation in a single API call:

```yaml
# Enhanced GitLab CI with Auto-Create
variables:
  DD_AUTO_CREATE_CONTEXT: "true"  # 🎯 Enable magic auto-creation!
  DD_PRODUCT_TYPE_NAME: "Web Applications"
  DD_PRODUCT_NAME: "E-Commerce Platform"
  DD_PRODUCT_DESCRIPTION: "Customer-facing e-commerce application"
  DD_PRODUCT_BUSINESS_CRITICALITY: "high"
  DD_PRODUCT_PLATFORM: "web"
  DD_PRODUCT_TAGS: "security,webapp,critical"
  DD_ENGAGEMENT_NAME: "Release 2.1 Security Testing"
  DD_ENGAGEMENT_DESCRIPTION: "Comprehensive security testing for major release"
  DD_APPLY_TAGS_TO_FINDINGS: "true"
  DD_FINDING_TAGS: "automated,trivy,container"

upload_security_scan:
  stage: upload
  image: osamamahmood/dd-import:latest
  variables:
    DD_TEST_NAME: "Container Security Scan"
    DD_TEST_TYPE_NAME: "Trivy Scan"
    DD_FILE_NAME: "trivy.json"
  script:
    - dd-reimport-findings.sh  # ✨ Single command, everything auto-created!
```

#### 📋 Traditional Workflow (Still Supported)

This snippet from a [GitLab CI pipeline](.gitlab-ci.yml) serves as an example how `dd-import` can be integrated using the traditional multi-step approach:

```yaml
variables:
  DD_PRODUCT_TYPE_NAME: "Showcase"
  DD_PRODUCT_NAME: "DefectDojo Importer"
  DD_ENGAGEMENT_NAME: "GitLab"

...

trivy:
  stage: test
  tags:
    - build
  variables:
    GIT_STRATEGY: none
  before_script:
    - export TRIVY_VERSION=$(wget -qO - "https://api.github.com/repos/aquasecurity/trivy/releases/latest" | grep '"tag_name":' | sed -E 's/.*"v([^"]+)".*/\1/')
    - echo $TRIVY_VERSION
    - wget --no-verbose https://github.com/aquasecurity/trivy/releases/download/v${TRIVY_VERSION}/trivy_${TRIVY_VERSION}_Linux-64bit.tar.gz -O - | tar -zxvf -
  allow_failure: true
  script:
    - ./trivy --exit-code 0 --no-progress -f json -o trivy.json osamamahmood/dd-import:latest
  artifacts:
    paths:
    - trivy.json
    when: always
    expire_in: 1 day

cloc:
  stage: test
  image: node:16
  tags:
    - build
  before_script:
    - npm install -g cloc
  script:
    - cloc src --json -out cloc.json
  artifacts:
    paths:
    - cloc.json
    when: always
    expire_in: 1 day

upload_trivy:
  stage: upload
  image: osamamahmood/dd-import:latest
  needs:
    - job: trivy
      artifacts: true  
  variables:
    GIT_STRATEGY: none
    DD_TEST_NAME: "Trivy"
    DD_TEST_TYPE_NAME: "Trivy Scan"
    DD_FILE_NAME: "trivy.json"
  script:
    - dd-reimport-findings.sh

upload-cloc:
  image: osamamahmood/dd-import:latest
  needs:
    - job: cloc
      artifacts: true  
  stage: upload
  tags:
    - build
  variables:
    DD_FILE_NAME: "cloc.json"
  script:
    - dd-import-languages.sh
```

- ***variables*** - Definition of some environment variables that will be used for several uploads. `DD_URL` and `DD_API_KEY` are not defined here because they are protected variables for the GitLab project.
- ***trivy*** - Example for a vulnerability scan with [trivy](https://github.com/aquasecurity/trivy). Output will be stored in JSON format (`trivy.json`).
- ***cloc*** - Example how to calculate the lines of code with [cloc](https://github.com/AlDanial/cloc). Output will be stored in JSON format (`cloc.json`).
- ***upload_trivy*** - This step will be executed after the `trivy` step, gets its output file and sets some variables specific for this step. Then the script to import the findings from this scan is executed.
- ***upload_cloc*** - This step will be executed after the `cloc` step, gets its output file and sets some variables specific for this step. Then the script to import the language data is executed.

Another example, showing how to use `dd-import` within a GitHub Action, can be found in [dd-import_example.yml](.github/workflows/dd-import_example.yml).

## 🚀 What's New in This Version

This enhanced version of `dd-import` introduces powerful new capabilities while maintaining 100% backward compatibility:

### ✨ Major Enhancements

- **🎯 Auto-Create Workflow**: Single API call creates all resources automatically (`DD_AUTO_CREATE_CONTEXT=true`)
- **📊 Rich Metadata**: Add business context with criticality, platform, lifecycle, and comprehensive tagging
- **🔄 Smart Workflow Selection**: Automatically chooses optimal workflow based on configuration
- **⚡ Retry Logic**: Exponential backoff for transient failures ensures reliable imports
- **✅ Enhanced Validation**: Comprehensive validation with helpful error messages
- **🏷️ Advanced Tagging**: Tag products, engagements, tests, and findings for better organization
- **🎛️ Finding Controls**: Fine-grained control over finding grouping and tag application

### 🔧 Technical Improvements

- **25+ New Environment Variables**: Extensive configuration options for all DefectDojo features
- **Robust Error Handling**: Better error messages and retry mechanisms
- **Input Validation**: Validates enum values and required fields before API calls
- **Response Validation**: Ensures API responses contain expected data
- **Performance Optimized**: Auto-create reduces API calls from 5+ to 1

### 📈 Migration Benefits

**Before (Traditional)**:
- Multiple API calls required (5+ calls)
- Manual resource management
- Basic metadata only
- No retry logic
- Generic error messages

**After (Enhanced)**:
- Optional single API call workflow
- Automatic resource creation
- Rich business metadata
- Robust retry mechanisms  
- Comprehensive validation and helpful error messages
- **100% backward compatible** - existing configs work unchanged!

## Developer guide

### Testing

`./bin/runUnitTests.sh` - Runs the unit tests and reports the test coverage.

`./bin/runDockerUnitTests.sh` - First creates the docker image and then starts a docker container in which the unit tests are executed.

## Acknowledgments

This project builds upon the excellent work of the original `dd-import` tool created by **Stefan Fleckenstein** at **MaibornWolff GmbH**. The original project can be found at [https://github.com/MaibornWolff/dd-import](https://github.com/MaibornWolff/dd-import).

Special thanks to Stefan and the MaibornWolff team for creating this valuable DefectDojo integration tool and making it available to the community. This enhanced version extends their foundation with additional features while maintaining full backward compatibility.

## License

Licensed under the [3-Clause BSD License](LICENSE.txt)
