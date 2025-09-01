#!/usr/bin/env python3
"""
Test script to verify all modules can be imported correctly
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_imports():
    """Test all module imports"""
    modules_to_test = [
        'cms',
        'cms.core.application',
        'cms.ui.pages.login_page',
        'cms.ui.pages.register_page',
        'cms.ui.pages.dashboard_page',
        'cms.ui.pages.users_page',
        'cms.services.database.database_service',
        'cms.services.auth.auth_service',
        'cms.services.email.email_service',
        'cms.ui.styles',
        'cms.ui.dialogs.message_box',
        'cms.utils.validators.validators',
        'cms.utils.helpers.icon_manager',
        'cms.config.settings',
    ]
    
    print("🧪 Testing module imports...")
    
    for module_name in modules_to_test:
        try:
            __import__(module_name)
            print(f"✅ {module_name}")
        except ImportError as e:
            print(f"❌ {module_name}: {e}")
        except Exception as e:
            print(f"⚠️ {module_name}: {e}")
    
    print("\n🎯 Testing main application import...")
    try:
        from cms import CustomerApp
        print("✅ CustomerApp imported successfully")
    except Exception as e:
        print(f"❌ CustomerApp import failed: {e}")

if __name__ == "__main__":
    test_imports()
