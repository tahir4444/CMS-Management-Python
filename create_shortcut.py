#!/usr/bin/env python3
"""
Create Windows Shortcut
Creates a Windows shortcut with custom icon
"""

import os
import sys

def create_shortcut():
    """Create a Windows shortcut with custom icon"""
    try:
        # Try to import required modules
        try:
            from win32com.client import Dispatch
        except ImportError:
            print("❌ pywin32 not found. Installing...")
            import subprocess
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pywin32"])
            from win32com.client import Dispatch
        
        # Get current directory and paths
        current_dir = os.getcwd()
        python_exe = sys.executable
        main_script = os.path.join(current_dir, "main.py")
        icon_path = os.path.join(current_dir, "app_icon.ico")
        shortcut_path = os.path.join(current_dir, "Customer Management System.lnk")
        
        # Create shortcut
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(shortcut_path)
        shortcut.Targetpath = python_exe
        shortcut.Arguments = f'"{main_script}"'
        shortcut.WorkingDirectory = current_dir
        shortcut.IconLocation = icon_path
        shortcut.save()
        
        print("✅ Shortcut created successfully!")
        print(f"📁 Location: {shortcut_path}")
        print("💡 Use this shortcut instead of running python main.py")
        return True
        
    except Exception as e:
        print(f"❌ Error creating shortcut: {str(e)}")
        return False

if __name__ == "__main__":
    print("Creating Windows shortcut with custom icon...")
    create_shortcut()
