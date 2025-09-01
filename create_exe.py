#!/usr/bin/env python3
"""
Create Executable Script
Creates a proper executable with custom icon for Windows
"""

import os
import sys
import subprocess

def create_executable():
    """Create an executable with custom icon"""
    try:
        # Check if PyInstaller is available
        try:
            import PyInstaller
            print("✅ PyInstaller found")
        except ImportError:
            print("❌ PyInstaller not found. Installing...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
            print("✅ PyInstaller installed")
        
        # Create the executable using the spec file for better control
        cmd = [
            "pyinstaller",
            "CustomerManagementSystem.spec"
        ]
        
        print("🔨 Creating executable with custom icon...")
        print(f"Command: {' '.join(cmd)}")
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Executable created successfully!")
            print("📁 Location: dist/CustomerManagementSystem.exe")
            print("💡 Run the .exe file instead of python main.py")
            return True
        else:
            print(f"❌ Error creating executable: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def create_batch_file():
    """Create a batch file that sets the icon properly"""
    batch_content = '''@echo off
title Customer Management System
cd /d "%~dp0"
python main.py
'''
    
    try:
        with open("run_cms.bat", "w") as f:
            f.write(batch_content)
        print("✅ Batch file created: run_cms.bat")
        return True
    except Exception as e:
        print(f"❌ Error creating batch file: {str(e)}")
        return False

def create_shortcut():
    """Create a Windows shortcut with custom icon"""
    try:
        import winshell
        from win32com.client import Dispatch
        
        # Get current directory
        current_dir = os.getcwd()
        exe_path = os.path.join(current_dir, "main.py")
        icon_path = os.path.join(current_dir, "app_icon.ico")
        
        # Create shortcut
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(os.path.join(current_dir, "Customer Management System.lnk"))
        shortcut.Targetpath = sys.executable
        shortcut.Arguments = f'"{exe_path}"'
        shortcut.WorkingDirectory = current_dir
        shortcut.IconLocation = icon_path
        shortcut.save()
        
        print("✅ Shortcut created: Customer Management System.lnk")
        return True
        
    except ImportError:
        print("ℹ️ Creating shortcut requires pywin32. Install with: pip install pywin32")
        return False
    except Exception as e:
        print(f"❌ Error creating shortcut: {str(e)}")
        return False

if __name__ == "__main__":
    print("Creating executable with custom icon...")
    
    # Try different methods
    print("\n1. Creating executable with PyInstaller...")
    if create_executable():
        print("🎉 Success! Use the .exe file for proper icon display.")
    else:
        print("\n2. Creating batch file...")
        create_batch_file()
        
        print("\n3. Creating shortcut...")
        create_shortcut()
        
        print("\n💡 Alternative solutions:")
        print("- Use the batch file: run_cms.bat")
        print("- Use the shortcut: Customer Management System.lnk")
        print("- Install pywin32: pip install pywin32")
