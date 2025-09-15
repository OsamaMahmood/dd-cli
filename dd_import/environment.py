import datetime
import os
from distutils.util import strtobool


class Environment:

    def __init__(self):
        self.url = os.getenv('DD_URL')
        self.api_key = os.getenv('DD_API_KEY')
        self.product_name = os.getenv('DD_PRODUCT_NAME')
        self.product_type_name = os.getenv('DD_PRODUCT_TYPE_NAME')
        self.engagement_name = os.getenv('DD_ENGAGEMENT_NAME')
        self.engagement_target_start = os.getenv('DD_ENGAGEMENT_TARGET_START', datetime.date.today().isoformat())
        self.engagement_target_end = os.getenv('DD_ENGAGEMENT_TARGET_END', '2999-12-31')
        self.test_name = os.getenv('DD_TEST_NAME')
        self.test_type_name = os.getenv('DD_TEST_TYPE_NAME')
        self.file_name = os.getenv('DD_FILE_NAME')
        self.active = os.getenv('DD_ACTIVE', 'True').lower() in ['true']
        self.verified = os.getenv('DD_VERIFIED', 'True').lower() in ['true']
        self.minimum_severity = os.getenv('DD_MINIMUM_SEVERITY', None)
        self.group_by = os.getenv('DD_GROUP_BY', None)
        self.push_to_jira = os.getenv('DD_PUSH_TO_JIRA', 'False').lower() in ['true']
        self.close_old_findings = os.getenv('DD_CLOSE_OLD_FINDINGS', 'True').lower() in ['true']
        self.close_old_findings_product_scope = os.getenv('DD_CLOSE_OLD_FINDINGS_PRODUCT_SCOPE', 'False').lower() in ['true']
        self.do_not_reactivate = os.getenv('DD_DO_NOT_REACTIVATE', 'False').lower() in ['true']
        self.version = os.getenv('DD_VERSION', None)
        self.endpoint_id = os.getenv('DD_ENDPOINT_ID', None)
        self.service = os.getenv('DD_SERVICE', None)
        self.build_id = os.getenv('DD_BUILD_ID', None)
        self.commit_hash = os.getenv('DD_COMMIT_HASH', None)
        self.branch_tag = os.getenv('DD_BRANCH_TAG', None)
        self.api_scan_configuration_id = os.getenv('DD_API_SCAN_CONFIGURATION_ID', None)
        self.source_code_management_uri = os.getenv('DD_SOURCE_CODE_MANAGEMENT_URI', None)
        self.ssl_verification = bool(strtobool(os.getenv('DD_SSL_VERIFY', 'true')))
        self.extra_header_1 = os.getenv('DD_EXTRA_HEADER_1')
        self.extra_header_2 = os.getenv('DD_EXTRA_HEADER_2')
        self.extra_header_1_value = os.getenv('DD_EXTRA_HEADER_1_VALUE')
        self.extra_header_2_value = os.getenv('DD_EXTRA_HEADER_2_VALUE')
        
        # NEW: Auto-creation and workflow control
        self.auto_create_context = os.getenv('DD_AUTO_CREATE_CONTEXT', 'False').lower() in ['true']
        self.deduplication_on_engagement = os.getenv('DD_DEDUPLICATION_ON_ENGAGEMENT', 'False').lower() in ['true']
        
        # NEW: Enhanced Product fields
        self.product_description = os.getenv('DD_PRODUCT_DESCRIPTION', None)
        self.product_business_criticality = os.getenv('DD_PRODUCT_BUSINESS_CRITICALITY', None)
        self.product_platform = os.getenv('DD_PRODUCT_PLATFORM', None)
        self.product_lifecycle = os.getenv('DD_PRODUCT_LIFECYCLE', None)
        self.product_origin = os.getenv('DD_PRODUCT_ORIGIN', None)
        self.product_user_records = os.getenv('DD_PRODUCT_USER_RECORDS', None)
        self.product_revenue = os.getenv('DD_PRODUCT_REVENUE', None)
        self.product_external_audience = os.getenv('DD_PRODUCT_EXTERNAL_AUDIENCE', 'False').lower() in ['true']
        self.product_internet_accessible = os.getenv('DD_PRODUCT_INTERNET_ACCESSIBLE', 'False').lower() in ['true']
        self.product_enable_simple_risk_acceptance = os.getenv('DD_PRODUCT_ENABLE_SIMPLE_RISK_ACCEPTANCE', 'True').lower() in ['true']
        self.product_enable_full_risk_acceptance = os.getenv('DD_PRODUCT_ENABLE_FULL_RISK_ACCEPTANCE', 'False').lower() in ['true']
        self.product_tags = os.getenv('DD_PRODUCT_TAGS', None)
        
        # NEW: Enhanced ProductType fields
        self.product_type_description = os.getenv('DD_PRODUCT_TYPE_DESCRIPTION', None)
        self.product_type_critical_product = os.getenv('DD_PRODUCT_TYPE_CRITICAL_PRODUCT', 'False').lower() in ['true']
        self.product_type_key_product = os.getenv('DD_PRODUCT_TYPE_KEY_PRODUCT', 'False').lower() in ['true']
        
        # NEW: Enhanced Engagement fields
        self.engagement_description = os.getenv('DD_ENGAGEMENT_DESCRIPTION', None)
        self.engagement_version = os.getenv('DD_ENGAGEMENT_VERSION', None)
        self.engagement_first_contacted = os.getenv('DD_ENGAGEMENT_FIRST_CONTACTED', None)
        self.engagement_reason = os.getenv('DD_ENGAGEMENT_REASON', None)
        self.engagement_tracker = os.getenv('DD_ENGAGEMENT_TRACKER', None)
        self.engagement_test_strategy = os.getenv('DD_ENGAGEMENT_TEST_STRATEGY', None)
        self.engagement_threat_model = os.getenv('DD_ENGAGEMENT_THREAT_MODEL', 'False').lower() in ['true']
        self.engagement_api_test = os.getenv('DD_ENGAGEMENT_API_TEST', 'False').lower() in ['true']
        self.engagement_pen_test = os.getenv('DD_ENGAGEMENT_PEN_TEST', 'False').lower() in ['true']
        self.engagement_check_list = os.getenv('DD_ENGAGEMENT_CHECK_LIST', 'False').lower() in ['true']
        self.engagement_status = os.getenv('DD_ENGAGEMENT_STATUS', 'In Progress')
        self.engagement_tags = os.getenv('DD_ENGAGEMENT_TAGS', None)
        
        # NEW: Enhanced Test fields
        self.test_description = os.getenv('DD_TEST_DESCRIPTION', None)
        self.test_version = os.getenv('DD_TEST_VERSION', None)
        self.test_tags = os.getenv('DD_TEST_TAGS', None)
        self.test_environment_name = os.getenv('DD_TEST_ENVIRONMENT_NAME', None)
        
        # NEW: Enhanced Finding/Import fields
        self.apply_tags_to_findings = os.getenv('DD_APPLY_TAGS_TO_FINDINGS', 'False').lower() in ['true']
        self.apply_tags_to_endpoints = os.getenv('DD_APPLY_TAGS_TO_ENDPOINTS', 'False').lower() in ['true']
        self.create_finding_groups_for_all_findings = os.getenv('DD_CREATE_FINDING_GROUPS_FOR_ALL_FINDINGS', 'True').lower() in ['true']
        self.finding_tags = os.getenv('DD_FINDING_TAGS', None)
        self.lead = os.getenv('DD_LEAD', None)

    def _parse_tags(self, tags_string):
        """Parse comma-separated tags string into list"""
        if tags_string is None or tags_string.strip() == '':
            return []
        return [tag.strip() for tag in tags_string.split(',') if tag.strip()]

    def _convert_to_int(self, value):
        """Convert string to integer, return None if invalid"""
        if value is None:
            return None
        try:
            return int(value)
        except (ValueError, TypeError):
            return None

    def get_product_tags_list(self):
        """Get product tags as list"""
        return self._parse_tags(self.product_tags)

    def get_engagement_tags_list(self):
        """Get engagement tags as list"""
        return self._parse_tags(self.engagement_tags)

    def get_test_tags_list(self):
        """Get test tags as list"""
        return self._parse_tags(self.test_tags)

    def get_finding_tags_list(self):
        """Get finding tags as list"""
        return self._parse_tags(self.finding_tags)

    def get_product_user_records_int(self):
        """Get product user records as integer"""
        return self._convert_to_int(self.product_user_records)

    def get_lead_int(self):
        """Get lead as integer"""
        return self._convert_to_int(self.lead)

    def check_environment_reimport_findings(self):
        error_string = self.check_environment_common()
        
        if self.auto_create_context:
            # Auto-create workflow - different validation rules
            error_string = self._validate_auto_create_workflow(error_string)
        else:
            # Traditional workflow - existing validation
            error_string = self._validate_traditional_workflow(error_string)
        
        # Common validation for both workflows
        if self.test_type_name is None:
            if error_string != '':
                error_string = error_string + ' / '
            error_string = error_string + 'DD_TEST_TYPE_NAME is missing'

        if len(error_string) > 0:
            raise Exception(error_string)

        # Print configuration values for debugging
        print('=== DD-IMPORT CONFIGURATION ===')
        if self.auto_create_context:
            print('🚀 AUTO-CREATE MODE ENABLED')
        print('DD_URL:                             ', self.url)
        print('DD_PRODUCT_TYPE_NAME:               ', self.product_type_name)
        print('DD_PRODUCT_NAME:                    ', self.product_name)
        print('DD_ENGAGEMENT_NAME:                 ', self.engagement_name)
        print('DD_ENGAGEMENT_TARGET_START:         ', self.engagement_target_start)
        print('DD_ENGAGEMENT_TARGET_END:           ', self.engagement_target_end)
        print('DD_TEST_NAME:                       ', self.test_name)
        print('DD_TEST_TYPE_NAME:                  ', self.test_type_name)
        print('DD_FILE_NAME:                       ', self.file_name)
        print('DD_ACTIVE:                          ', self.active)
        print('DD_VERIFIED:                        ', self.verified)
        print('DD_MINIMUM_SEVERITY:                ', self.minimum_severity)
        print('DD_GROUP_BY:                        ', self.group_by)
        print('DD_PUSH_TO_JIRA:                    ', self.push_to_jira)
        print('DD_CLOSE_OLD_FINDINGS:              ', self.close_old_findings)
        print('DD_CLOSE_OLD_FINDINGS_PRODUCT_SCOPE:', self.close_old_findings_product_scope)
        print('DD_DO_NOT_REACTIVATE:               ', self.do_not_reactivate)
        print('DD_VERSION:                         ', self.version)
        print('DD_ENDPOINT_ID:                     ', self.endpoint_id)
        print('DD_SERVICE:                         ', self.service)
        print('DD_BUILD_ID:                        ', self.build_id)
        print('DD_COMMIT_HASH:                     ', self.commit_hash)
        print('DD_BRANCH_TAG:                      ', self.branch_tag)
        print('DD_API_SCAN_CONFIGURATION_ID:       ', self.api_scan_configuration_id)
        print('DD_SOURCE_CODE_MANAGEMENT_URI:      ', self.source_code_management_uri)
        print('DD_SSL_VERIFY:                      ', self.ssl_verification)
        print('DD_EXTRA_HEADER_1:                  ', self.extra_header_1)
        print('DD_EXTRA_HEADER_2:                  ', self.extra_header_2)
        
        # Print new enhanced fields if they are set
        if self.auto_create_context or any([
            self.product_description, self.product_business_criticality, self.product_platform,
            self.engagement_description, self.apply_tags_to_findings
        ]):
            print('\n=== ENHANCED FEATURES ===')
            print('DD_AUTO_CREATE_CONTEXT:             ', self.auto_create_context)
            if self.product_description:
                print('DD_PRODUCT_DESCRIPTION:             ', self.product_description)
            if self.product_business_criticality:
                print('DD_PRODUCT_BUSINESS_CRITICALITY:    ', self.product_business_criticality)
            if self.product_platform:
                print('DD_PRODUCT_PLATFORM:                ', self.product_platform)
            if self.product_tags:
                print('DD_PRODUCT_TAGS:                    ', self.product_tags)
            if self.engagement_description:
                print('DD_ENGAGEMENT_DESCRIPTION:          ', self.engagement_description)
            if self.apply_tags_to_findings:
                print('DD_APPLY_TAGS_TO_FINDINGS:          ', self.apply_tags_to_findings)
            if self.finding_tags:
                print('DD_FINDING_TAGS:                    ', self.finding_tags)
        print('')

    def _validate_auto_create_workflow(self, error_string):
        """Validate environment for auto-create workflow"""
        # For auto-create, engagement_name and test_name are optional
        # They will be created automatically by DefectDojo if not provided
        
        # Validate enum fields have correct values
        if self.product_business_criticality is not None:
            valid_criticalities = ['very high', 'high', 'medium', 'low', 'very low', 'none']
            if self.product_business_criticality not in valid_criticalities:
                if error_string != '':
                    error_string = error_string + ' / '
                error_string = error_string + f'DD_PRODUCT_BUSINESS_CRITICALITY must be one of: {", ".join(valid_criticalities)}'
        
        if self.product_platform is not None:
            valid_platforms = ['web service', 'desktop', 'iot', 'mobile', 'web']
            if self.product_platform not in valid_platforms:
                if error_string != '':
                    error_string = error_string + ' / '
                error_string = error_string + f'DD_PRODUCT_PLATFORM must be one of: {", ".join(valid_platforms)}'
        
        if self.product_lifecycle is not None:
            valid_lifecycles = ['construction', 'production', 'retirement']
            if self.product_lifecycle not in valid_lifecycles:
                if error_string != '':
                    error_string = error_string + ' / '
                error_string = error_string + f'DD_PRODUCT_LIFECYCLE must be one of: {", ".join(valid_lifecycles)}'
        
        return error_string

    def _validate_traditional_workflow(self, error_string):
        """Validate environment for traditional workflow"""
        if self.engagement_name is None:
            if error_string != '':
                error_string = error_string + ' / '
            error_string = error_string + 'DD_ENGAGEMENT_NAME is missing'
        if self.test_name is None:
            if error_string != '':
                error_string = error_string + ' / '
            error_string = error_string + 'DD_TEST_NAME is missing'
        
        return error_string

    def check_environment_languages(self):
        error_string = self.check_environment_common()

        if self.file_name is None:
            if error_string != '':
                error_string = error_string + ' / '
            error_string = error_string + 'DD_FILE_NAME is missing'

        if len(error_string) > 0:
            raise Exception(error_string)

        print('DD_URL:                ', self.url)
        print('DD_PRODUCT_TYPE_NAME:  ', self.product_type_name)
        print('DD_PRODUCT_NAME:       ', self.product_name)
        print('DD_FILE_NAME:          ', self.file_name)
        print('DD_SSL_VERIFY:         ', self.ssl_verification)
        print('')

    def check_environment_common(self):
        error_string = ''
        if self.url is None:
            error_string = 'DD_URL is missing'
        if self.api_key is None:
            if error_string != '':
                error_string = error_string + ' / '
            error_string = error_string + 'DD_API_KEY is missing'
        if self.product_type_name is None:
            if error_string != '':
                error_string = error_string + ' / '
            error_string = error_string + 'DD_PRODUCT_TYPE_NAME is missing'
        if self.product_name is None:
            if error_string != '':
                error_string = error_string + ' / '
            error_string = error_string + 'DD_PRODUCT_NAME is missing'

        return error_string
