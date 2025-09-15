from dd_import.dd_api import Api
from dd_import.environment import Environment


def dd_reimport_findings():
    try:
        environment = Environment()
        environment.check_environment_reimport_findings()
        api = Api()
        
        # Smart workflow selection based on DD_AUTO_CREATE_CONTEXT
        if environment.auto_create_context:
            print("🚀 Using AUTO-CREATE workflow (single API call)")
            print("   DefectDojo will create all resources automatically...")
            api.reimport_scan_with_auto_create()
        else:
            print("📋 Using TRADITIONAL workflow (multiple API calls)")
            print("   Creating/finding resources step by step...")
            product_type_id = api.get_product_type()
            product_id = api.get_product(product_type_id)
            engagement_id = api.get_engagement(product_id)
            test_id = api.get_test(engagement_id)
            api.reimport_scan(test_id)
            api.update_engagement(engagement_id)
            
        print("✅ Import completed successfully!")
        
    except Exception as e:
        print(f"❌ Error during import: {str(e)}")
        exit(1)


if __name__ == '__main__':
    dd_reimport_findings()
