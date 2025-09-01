#!/usr/bin/env python3
"""
Enterprise CMS - Main Entry Point
Professional Customer Management System

This is the main entry point for the Enterprise CMS application.
"""

import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

import tkinter as tk
from cms import CustomerApp


def main():
    """Main application entry point"""
    try:
        # Create the main window
        root = tk.Tk()
        
        # Create and run the application
        app = CustomerApp(root)
        app.run()
        
    except Exception as e:
        print(f"Error starting application: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
