#!/usr/bin/env python3
"""
CMS Launcher
Simple launcher script that can be pinned to taskbar
"""

import os
import sys
import subprocess

def main():
    """Launch the Customer Management System"""
    try:
        # Get the directory where this script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Path to the executable
        exe_path = os.path.join(script_dir, "dist", "CustomerManagementSystem.exe")
        
        # Check if executable exists
        if not os.path.exists(exe_path):
            print("❌ Executable not found!")
            print("Please run create_exe.py first to create the executable.")
            input("Press Enter to exit...")
            return
        
        # Launch the executable
        print("🚀 Launching Customer Management System...")
        subprocess.Popen([exe_path], cwd=script_dir)
        
    except Exception as e:
        print(f"❌ Error launching CMS: {str(e)}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()
