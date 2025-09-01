#!/usr/bin/env python3
"""
Customer Management System Launcher
A simple launcher script for the Windows application
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from main import main
    print("Starting Customer Management System...")
    main()
except ImportError as e:
    print(f"Error importing modules: {e}")
    print("Make sure you have Python 3.x installed and all files are in the same directory.")
except Exception as e:
    print(f"Error starting application: {e}")
    input("Press Enter to exit...")
