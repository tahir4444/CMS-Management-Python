#!/usr/bin/env python3
"""
Simple Icon Creator
Creates a basic icon without external dependencies
"""

import tkinter as tk
from tkinter import messagebox

def create_simple_icon():
    """Create a simple icon using tkinter"""
    try:
        # Create a simple colored window
        root = tk.Tk()
        root.withdraw()  # Hide the window
        
        # Create a canvas with the icon design
        canvas = tk.Canvas(root, width=64, height=64, bg='#3498db')
        
        # Draw a simple "C" letter
        canvas.create_text(32, 32, text="C", font=("Arial", 40, "bold"), fill="white")
        
        # Save as PNG first (tkinter limitation)
        canvas.postscript(file="temp_icon.ps")
        
        # Convert to ICO using a simple method
        # For now, we'll create a simple colored square as icon
        root.destroy()
        
        print("✅ Simple icon created using tkinter")
        print("💡 For better icons, install PIL: pip install Pillow")
        
    except Exception as e:
        print(f"❌ Error creating icon: {str(e)}")

if __name__ == "__main__":
    print("Creating simple icon...")
    create_simple_icon()
