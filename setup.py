#!/usr/bin/env python3
"""
Enterprise CMS - Setup Script
Automated setup for new developers
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 or higher is required")
        print(f"Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible")
    return True

def create_virtual_environment():
    """Create virtual environment if it doesn't exist"""
    venv_path = Path(".venv")
    if venv_path.exists():
        print("✅ Virtual environment already exists")
        return True
    
    return run_command("python -m venv .venv", "Creating virtual environment")

def install_dependencies():
    """Install required dependencies"""
    # Determine the correct pip command for the virtual environment
    if os.name == 'nt':  # Windows
        pip_cmd = ".venv\\Scripts\\pip"
    else:  # Unix/Linux/Mac
        pip_cmd = ".venv/bin/pip"
    
    return run_command(f"{pip_cmd} install -r requirements.txt", "Installing dependencies")

def setup_smtp_config():
    """Set up SMTP configuration from template"""
    smtp_config = Path("smtp_config.py")
    smtp_template = Path("smtp_config_template.py")
    
    if smtp_config.exists():
        print("✅ SMTP configuration already exists")
        return True
    
    if smtp_template.exists():
        shutil.copy(smtp_template, smtp_config)
        print("✅ SMTP configuration created from template")
        print("⚠️  Remember to update smtp_config.py with your actual credentials")
        return True
    else:
        print("❌ SMTP template not found")
        return False

def create_directories():
    """Create necessary directories"""
    directories = ["logs", "temp", "uploads", "backups"]
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
    print("✅ Created necessary directories")

def main():
    """Main setup function"""
    print("🚀 Enterprise CMS - Setup Script")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Create virtual environment
    if not create_virtual_environment():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        sys.exit(1)
    
    # Set up SMTP configuration
    setup_smtp_config()
    
    # Create directories
    create_directories()
    
    print("\n🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Activate virtual environment:")
    if os.name == 'nt':  # Windows
        print("   .venv\\Scripts\\activate")
    else:  # Unix/Linux/Mac
        print("   source .venv/bin/activate")
    print("2. Update smtp_config.py with your SMTP credentials")
    print("3. Run the application: python main.py")
    print("4. Build executable: python create_exe.py")
    
    print("\n📚 For more information, see README.md")

if __name__ == "__main__":
    main()
