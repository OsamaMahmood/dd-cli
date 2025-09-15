import datetime
import json
import time

import requests
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning

from dd_import.environment import Environment

# Disable SSL Warnings
disable_warnings(InsecureRequestWarning)


# Fix for reimport without file, see https://github.com/psf/requests/issues/1081#issuecomment-428504128
class ForceMultipartDict(dict):
    def __bool__(self):
        return True


FORCE_MULTIPART = ForceMultipartDict()  # An empty dict that boolean-evaluates as `True`.


class Api:

    def __init__(self):
        self.environment = Environment()
        self.headers = {'Content-type': 'application/json', 'Authorization': 'Token ' + self.environment.api_key}

        if self.environment.extra_header_1 and self.environment.extra_header_1_value is not None:
            self.headers.update({self.environment.extra_header_1: self.environment.extra_header_1_value})

        if self.environment.extra_header_2 and self.environment.extra_header_2_value is not None:
            self.headers.update({self.environment.extra_header_2: self.environment.extra_header_2_value})

        self.headers_without_json = {'Authorization': 'Token ' + self.environment.api_key}

        if self.environment.extra_header_1 and self.environment.extra_header_1_value is not None:
            self.headers_without_json.update({self.environment.extra_header_1: self.environment.extra_header_1_value})

        if self.environment.extra_header_2 and self.environment.extra_header_2_value is not None:
            self.headers_without_json.update({self.environment.extra_header_2: self.environment.extra_header_2_value})

        self.product_type_url = self.environment.url + '/api/v2/product_types/'
        self.product_url = self.environment.url + '/api/v2/products/'
        self.engagement_url = self.environment.url + '/api/v2/engagements/'
        self.test_url = self.environment.url + '/api/v2/tests/'
        self.test_type_url = self.environment.url + '/api/v2/test_types/'
        self.reimport_scan_url = self.environment.url + '/api/v2/reimport-scan/'
        self.import_languages_url = self.environment.url + '/api/v2/import-languages/'
        self.ssl_verification = self.environment.ssl_verification

    def _make_request_with_retry(self, method, url, max_retries=3, backoff_factor=1, **kwargs):
        """
        Make HTTP requests with exponential backoff retry logic.
        
        Args:
            method: HTTP method (GET, POST, PATCH)
            url: Request URL
            max_retries: Maximum number of retry attempts
            backoff_factor: Backoff multiplier for retry delays
            **kwargs: Additional arguments passed to requests method
            
        Returns:
            requests.Response object
            
        Raises:
            Exception: If all retry attempts fail
        """
        for attempt in range(max_retries + 1):
            try:
                response = getattr(requests, method.lower())(url, **kwargs)
                response.raise_for_status()
                return response
                
            except requests.exceptions.RequestException as e:
                if attempt == max_retries:
                    # Last attempt failed, raise the exception
                    raise Exception(f"API request failed after {max_retries} retries: {str(e)}")
                    
                # Calculate retry delay with exponential backoff
                delay = backoff_factor * (2 ** attempt)
                print(f"⚠️  Request failed (attempt {attempt + 1}/{max_retries + 1}), retrying in {delay}s...")
                print(f"   Error: {str(e)}")
                time.sleep(delay)
                
        # This should never be reached, but just in case
        raise Exception(f"Unexpected error in retry logic")

    def _validate_response_data(self, response_data, expected_keys=None):
        """
        Validate API response data structure.
        
        Args:
            response_data: Parsed JSON response
            expected_keys: List of keys that should be present in response
            
        Returns:
            bool: True if validation passes
            
        Raises:
            Exception: If validation fails
        """
        if not isinstance(response_data, dict):
            raise Exception(f"Invalid response format: expected dict, got {type(response_data)}")
            
        if expected_keys:
            missing_keys = [key for key in expected_keys if key not in response_data]
            if missing_keys:
                raise Exception(f"Missing required keys in response: {missing_keys}")
                
        return True

    def get_product_type(self):
        payload = {'name': self.environment.product_type_name}
        r = requests.get(self.product_type_url,
                         headers=self.headers,
                         params=payload,
                         verify=self.ssl_verification)
        r.raise_for_status()
        product_type_data = json.loads(r.text)
        for product_type in product_type_data.get('results', []):
            if product_type.get('name', '') == self.environment.product_type_name:
                product_type_id = product_type['id']
                print('Product type found, id: ', product_type_id)
                return product_type_id
        return self.new_product_type(self.environment.product_type_name)

    def new_product_type(self, product_type_name):
        payload = {'name': product_type_name}
        
        # Add enhanced ProductType fields
        if self.environment.product_type_description is not None:
            payload['description'] = self.environment.product_type_description
        if self.environment.product_type_critical_product:
            payload['critical_product'] = self.environment.product_type_critical_product
        if self.environment.product_type_key_product:
            payload['key_product'] = self.environment.product_type_key_product
            
        r = requests.post(self.product_type_url,
                          headers=self.headers,
                          data=json.dumps(payload),
                          verify=self.ssl_verification)
        r.raise_for_status()
        product_type_data = json.loads(r.text)
        print('New product type,   id: ', product_type_data['id'])
        return product_type_data['id']

    def get_product(self, product_type):
        payload = {'name': self.environment.product_name,
                   'prod_type': product_type}
        r = requests.get(self.product_url,
                         headers=self.headers,
                         params=payload,
                         verify=self.ssl_verification)
        r.raise_for_status()
        product_data = json.loads(r.text)
        for product in product_data.get('results', []):
            if product.get('name', '') == self.environment.product_name:
                product_id = product['id']
                print('Product found,      id: ', product_id)
                return product_id
        return self.new_product(product_type)

    def new_product(self, product_type):
        payload = {
            'name': self.environment.product_name,
            'description': self.environment.product_description or self.environment.product_name,
            'prod_type': product_type
        }
        
        # Add enhanced Product fields
        if self.environment.product_business_criticality is not None:
            payload['business_criticality'] = self.environment.product_business_criticality
        if self.environment.product_platform is not None:
            payload['platform'] = self.environment.product_platform
        if self.environment.product_lifecycle is not None:
            payload['lifecycle'] = self.environment.product_lifecycle
        if self.environment.product_origin is not None:
            payload['origin'] = self.environment.product_origin
        if self.environment.product_user_records is not None:
            payload['user_records'] = self.environment.get_product_user_records_int()
        if self.environment.product_revenue is not None:
            payload['revenue'] = self.environment.product_revenue
        if self.environment.product_external_audience:
            payload['external_audience'] = self.environment.product_external_audience
        if self.environment.product_internet_accessible:
            payload['internet_accessible'] = self.environment.product_internet_accessible
        if self.environment.product_enable_simple_risk_acceptance is not None:
            payload['enable_simple_risk_acceptance'] = self.environment.product_enable_simple_risk_acceptance
        if self.environment.product_enable_full_risk_acceptance:
            payload['enable_full_risk_acceptance'] = self.environment.product_enable_full_risk_acceptance
            
        # Add tags if provided
        product_tags = self.environment.get_product_tags_list()
        if product_tags:
            payload['tags'] = product_tags
            
        r = requests.post(self.product_url,
                          headers=self.headers,
                          data=json.dumps(payload),
                          verify=self.ssl_verification)
        r.raise_for_status()
        product_data = json.loads(r.text)
        print('New product,        id: ', product_data['id'])
        return product_data['id']

    def get_engagement(self, product):
        payload = {'name': self.environment.engagement_name,
                   'product': product}
        r = requests.get(self.engagement_url,
                         headers=self.headers,
                         params=payload,
                         verify=self.ssl_verification)
        r.raise_for_status()
        engagement_data = json.loads(r.text)
        for engagement in engagement_data.get('results', []):
            if engagement.get('name', '') == self.environment.engagement_name:
                engagement_id = engagement['id']
                print('Engagement found,   id: ', engagement_id)
                return engagement_id
        return self.new_engagement(product)

    def new_engagement(self, product):
        payload = {
            'name': self.environment.engagement_name,
            'product': product,
            'target_start': self.environment.engagement_target_start,
            'target_end': self.environment.engagement_target_end,
            'engagement_type': 'CI/CD',
            'status': self.environment.engagement_status
        }
        
        # Add enhanced Engagement fields
        if self.environment.engagement_description is not None:
            payload['description'] = self.environment.engagement_description
        if self.environment.engagement_version is not None:
            payload['version'] = self.environment.engagement_version
        if self.environment.engagement_first_contacted is not None:
            payload['first_contacted'] = self.environment.engagement_first_contacted
        if self.environment.engagement_reason is not None:
            payload['reason'] = self.environment.engagement_reason
        if self.environment.engagement_tracker is not None:
            payload['tracker'] = self.environment.engagement_tracker
        if self.environment.engagement_test_strategy is not None:
            payload['test_strategy'] = self.environment.engagement_test_strategy
        if self.environment.engagement_threat_model:
            payload['threat_model'] = self.environment.engagement_threat_model
        if self.environment.engagement_api_test:
            payload['api_test'] = self.environment.engagement_api_test
        if self.environment.engagement_pen_test:
            payload['pen_test'] = self.environment.engagement_pen_test
        if self.environment.engagement_check_list:
            payload['check_list'] = self.environment.engagement_check_list
        if self.environment.source_code_management_uri is not None:
            payload['source_code_management_uri'] = self.environment.source_code_management_uri
            
        # Add tags if provided
        engagement_tags = self.environment.get_engagement_tags_list()
        if engagement_tags:
            payload['tags'] = engagement_tags
            
        r = requests.post(self.engagement_url,
                          headers=self.headers,
                          data=json.dumps(payload),
                          verify=self.ssl_verification)
        r.raise_for_status()
        engagement_data = json.loads(r.text)
        print('New engagement,     id: ', engagement_data['id'])
        return engagement_data['id']

    def update_engagement(self, engagement):
        if self.environment.build_id is not None or \
           self.environment.commit_hash is not None or \
           self.environment.branch_tag is not None:
            payload = {'build_id': self.environment.build_id,
                       'commit_hash': self.environment.commit_hash,
                       'branch_tag': self.environment.branch_tag}
            r = requests.patch(self.engagement_url + str(engagement) + '/',
                               headers=self.headers,
                               data=json.dumps(payload),
                               verify=self.ssl_verification)
            r.raise_for_status()

    def get_test(self, engagement):
        payload = {'title': self.environment.test_name,
                   'engagement': engagement}
        r = requests.get(self.test_url,
                         headers=self.headers,
                         params=payload,
                         verify=self.ssl_verification)
        r.raise_for_status()
        test_data = json.loads(r.text)
        for test in test_data.get('results', []):
            if test.get('title', '') == self.environment.test_name:
                test_id = test['id']
                print('Test found,         id: ', test_id)
                return test_id
        return self.new_test(engagement)

    def new_test(self, engagement):
        today = datetime.date.today()
        today = datetime.datetime(today.year, today.month, today.day)
        payload = {
            'title': self.environment.test_name,
            'engagement': engagement,
            'target_start': today.isoformat(),
            'target_end': datetime.datetime.fromisoformat('2999-12-31').isoformat(),
            'test_type': self.get_test_type()
        }
        
        # Add enhanced Test fields
        if self.environment.test_description is not None:
            payload['description'] = self.environment.test_description
        if self.environment.test_version is not None:
            payload['version'] = self.environment.test_version
        if self.environment.build_id is not None:
            payload['build_id'] = self.environment.build_id
        if self.environment.commit_hash is not None:
            payload['commit_hash'] = self.environment.commit_hash
        if self.environment.branch_tag is not None:
            payload['branch_tag'] = self.environment.branch_tag
        if self.environment.get_lead_int() is not None:
            payload['lead'] = self.environment.get_lead_int()
        if self.environment.api_scan_configuration_id is not None:
            payload['api_scan_configuration'] = self.environment.api_scan_configuration_id
            
        # Add tags if provided
        test_tags = self.environment.get_test_tags_list()
        if test_tags:
            payload['tags'] = test_tags
            
        r = requests.post(self.test_url,
                          headers=self.headers,
                          data=json.dumps(payload),
                          verify=self.ssl_verification)
        r.raise_for_status()
        test_data = json.loads(r.text)
        print('New test,           id: ', test_data['id'])
        return test_data['id']

    def get_test_type(self):
        payload = {'name': self.environment.test_type_name}
        r = requests.get(self.test_type_url,
                         headers=self.headers,
                         params=payload,
                         verify=self.ssl_verification)
        r.raise_for_status()
        test_type_data = json.loads(r.text)
        for test_type in test_type_data.get('results', []):
            if test_type.get('name', '') == self.environment.test_type_name:
                return test_type['id']
        raise Exception(f'Test type {self.environment.test_type_name} not found')

    def reimport_scan(self, test):
        payload = {'scan_date': datetime.date.today().isoformat(),
                   'scan_type': self.environment.test_type_name,
                   'test': test,
                   'active': self.environment.active,
                   'verified': self.environment.verified,
                   'push_to_jira': self.environment.push_to_jira,
                   'close_old_findings': self.environment.close_old_findings,
                   'close_old_findings_product_scope': self.environment.close_old_findings_product_scope,
                   'do_not_reactivate': self.environment.do_not_reactivate
                   }
        if self.environment.minimum_severity is not None:
            payload['minimum_severity'] = self.environment.minimum_severity
        if self.environment.group_by is not None:
            payload['group_by'] = self.environment.group_by
        if self.environment.version is not None:
            payload['version'] = self.environment.version
        if self.environment.endpoint_id is not None:
            payload['endpoint_to_add'] = int(self.environment.endpoint_id)
        if self.environment.service is not None:
            payload['service'] = self.environment.service
        if self.environment.api_scan_configuration_id is not None:
            payload['api_scan_configuration'] = self.environment.api_scan_configuration_id
        if self.environment.source_code_management_uri is not None:
            payload['source_code_management_uri'] = self.environment.source_code_management_uri

        if self.environment.file_name is not None:
            files = {'file': (self.environment.file_name,
                              open(self.environment.file_name, 'rb'),
                              'application/json', {'Expires': '0'})}
            response = requests.post(self.reimport_scan_url,
                                     headers=self.headers_without_json,
                                     data=payload,
                                     files=files,
                                     verify=self.ssl_verification)
        else:
            response = requests.post(self.reimport_scan_url,
                                     headers=self.headers_without_json,
                                     data=payload,
                                     files=FORCE_MULTIPART,
                                     verify=self.ssl_verification)

        response.raise_for_status()

        print()
        print('Scan results imported')

    def reimport_scan_with_auto_create(self):
        """
        Enhanced reimport scan using DefectDojo's auto-create functionality.
        This method can create products, engagements, and tests automatically
        in a single API call using the auto_create_context feature.
        """
        payload = {
            'scan_date': datetime.date.today().isoformat(),
            'scan_type': self.environment.test_type_name,
            'active': self.environment.active,
            'verified': self.environment.verified,
            'push_to_jira': self.environment.push_to_jira,
            'close_old_findings': self.environment.close_old_findings,
            'close_old_findings_product_scope': self.environment.close_old_findings_product_scope,
            'do_not_reactivate': self.environment.do_not_reactivate,
            
            # AUTO-CREATE CONTEXT - This enables the magic!
            'auto_create_context': True,
            'product_type_name': self.environment.product_type_name,
            'product_name': self.environment.product_name,
        }

        # Add optional auto-create fields
        if self.environment.engagement_name is not None:
            payload['engagement_name'] = self.environment.engagement_name
        if self.environment.test_name is not None:
            payload['test_title'] = self.environment.test_name
        if self.environment.deduplication_on_engagement:
            payload['deduplication_on_engagement'] = self.environment.deduplication_on_engagement
        
        # Enhanced Product fields
        if self.environment.product_description is not None:
            payload['product_description'] = self.environment.product_description
        if self.environment.product_business_criticality is not None:
            payload['business_criticality'] = self.environment.product_business_criticality
        if self.environment.product_platform is not None:
            payload['platform'] = self.environment.product_platform
        if self.environment.product_lifecycle is not None:
            payload['lifecycle'] = self.environment.product_lifecycle
        if self.environment.product_origin is not None:
            payload['origin'] = self.environment.product_origin
        if self.environment.product_external_audience:
            payload['external_audience'] = self.environment.product_external_audience
        if self.environment.product_internet_accessible:
            payload['internet_accessible'] = self.environment.product_internet_accessible

        # Enhanced Engagement fields  
        if self.environment.engagement_target_end != '2999-12-31':
            payload['engagement_end_date'] = self.environment.engagement_target_end
        if self.environment.engagement_description is not None:
            payload['engagement_description'] = self.environment.engagement_description
        if self.environment.engagement_version is not None:
            payload['engagement_version'] = self.environment.engagement_version
        
        # Enhanced Finding/Import controls
        if self.environment.apply_tags_to_findings:
            payload['apply_tags_to_findings'] = self.environment.apply_tags_to_findings
        if self.environment.apply_tags_to_endpoints:
            payload['apply_tags_to_endpoints'] = self.environment.apply_tags_to_endpoints
        if not self.environment.create_finding_groups_for_all_findings:
            payload['create_finding_groups_for_all_findings'] = self.environment.create_finding_groups_for_all_findings

        # Add all existing optional fields
        if self.environment.minimum_severity is not None:
            payload['minimum_severity'] = self.environment.minimum_severity
        if self.environment.group_by is not None:
            payload['group_by'] = self.environment.group_by
        if self.environment.version is not None:
            payload['version'] = self.environment.version
        if self.environment.endpoint_id is not None:
            payload['endpoint_to_add'] = int(self.environment.endpoint_id)
        if self.environment.service is not None:
            payload['service'] = self.environment.service
        if self.environment.build_id is not None:
            payload['build_id'] = self.environment.build_id
        if self.environment.commit_hash is not None:
            payload['commit_hash'] = self.environment.commit_hash
        if self.environment.branch_tag is not None:
            payload['branch_tag'] = self.environment.branch_tag
        if self.environment.api_scan_configuration_id is not None:
            payload['api_scan_configuration'] = self.environment.api_scan_configuration_id
        if self.environment.source_code_management_uri is not None:
            payload['source_code_management_uri'] = self.environment.source_code_management_uri
        if self.environment.get_lead_int() is not None:
            payload['lead'] = self.environment.get_lead_int()
        if self.environment.test_environment_name is not None:
            payload['environment'] = self.environment.test_environment_name

        # Handle file upload with retry logic
        try:
            if self.environment.file_name is not None:
                files = {'file': (self.environment.file_name,
                                  open(self.environment.file_name, 'rb'),
                                  'application/json', {'Expires': '0'})}
                response = self._make_request_with_retry(
                    'POST', self.reimport_scan_url,
                    headers=self.headers_without_json,
                    data=payload,
                    files=files,
                    verify=self.ssl_verification,
                    max_retries=3
                )
            else:
                response = self._make_request_with_retry(
                    'POST', self.reimport_scan_url,
                    headers=self.headers_without_json,
                    data=payload,
                    files=FORCE_MULTIPART,
                    verify=self.ssl_verification,
                    max_retries=3
                )
                
            # Validate response
            response_data = json.loads(response.text)
            self._validate_response_data(response_data, expected_keys=['scan_type'])
            
        except Exception as e:
            raise Exception(f"Auto-create reimport failed: {str(e)}")

        print()
        print('🚀 Scan results imported using AUTO-CREATE mode!')
        print('✅ Resources created/updated automatically by DefectDojo')

    def import_languages(self, product):
        payload = {'product': product}
        files = {'file': (self.environment.file_name,
                 open(self.environment.file_name, 'rb'),
                 'application/json', {'Expires': '0'})}

        response = requests.post(self.import_languages_url,
                                 headers=self.headers_without_json,
                                 data=payload,
                                 files=files,
                                 verify=self.ssl_verification)
        response.raise_for_status()

        print()
        print('Languages imported')
