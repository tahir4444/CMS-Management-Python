#!/usr/bin/env python3
"""
Create Desktop Shortcut
Creates a desktop shortcut for the Customer Management System
"""

import os
import sys
import subprocess

def create_desktop_shortcut():
    """Create a desktop shortcut for the CMS executable"""
    try:
        # Get desktop path
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        if not os.path.exists(desktop):
            print("❌ Desktop folder not found")
            return False
        
        # Get current directory and paths
        current_dir = os.getcwd()
        exe_path = os.path.join(current_dir, "dist", "CustomerManagementSystem.exe")
        icon_path = os.path.join(current_dir, "app_icon.ico")
        shortcut_path = os.path.join(desktop, "Customer Management System.lnk")
        
        # Check if executable exists
        if not os.path.exists(exe_path):
            print("❌ Executable not found. Run create_exe.py first.")
            return False
        
        # Try to create shortcut using PowerShell (built-in)
        ps_script = f'''
$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("{shortcut_path}")
$Shortcut.TargetPath = "{exe_path}"
$Shortcut.WorkingDirectory = "{current_dir}"
$Shortcut.IconLocation = "{icon_path}"
$Shortcut.Save()
'''
        
        # Run PowerShell script
        result = subprocess.run([
            "powershell", "-Command", ps_script
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Desktop shortcut created successfully!")
            print(f"📁 Location: {shortcut_path}")
            print("💡 You can now run CMS from your desktop!")
            return True
        else:
            print(f"❌ Error creating shortcut: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def create_start_menu_shortcut():
    """Create a start menu shortcut"""
    try:
        # Get start menu path
        start_menu = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs")
        if not os.path.exists(start_menu):
            print("❌ Start Menu folder not found")
            return False
        
        # Create shortcut in start menu
        shortcut_path = os.path.join(start_menu, "Customer Management System.lnk")
        exe_path = os.path.join(os.getcwd(), "dist", "CustomerManagementSystem.exe")
        icon_path = os.path.join(os.getcwd(), "app_icon.ico")
        
        ps_script = f'''
$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("{shortcut_path}")
$Shortcut.TargetPath = "{exe_path}"
$Shortcut.WorkingDirectory = "{os.getcwd()}"
$Shortcut.IconLocation = "{icon_path}"
$Shortcut.Save()
'''
        
        result = subprocess.run([
            "powershell", "-Command", ps_script
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Start Menu shortcut created successfully!")
            print(f"📁 Location: {shortcut_path}")
            return True
        else:
            print(f"❌ Error creating start menu shortcut: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

if __name__ == "__main__":
    print("Creating shortcuts for Customer Management System...")
    
    print("\n1. Creating Desktop Shortcut...")
    create_desktop_shortcut()
    
    print("\n2. Creating Start Menu Shortcut...")
    create_start_menu_shortcut()
    
    print("\n💡 Now you can run CMS in multiple ways:")
    print("- Double-click the desktop shortcut")
    print("- Use Start Menu → Customer Management System")
    print("- Run run_cms.bat")
    print("- Run dist\\CustomerManagementSystem.exe directly")
