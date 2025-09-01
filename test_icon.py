#!/usr/bin/env python3
"""
Icon Test Script
Tests if the custom icon is working properly
"""

import tkinter as tk
import os

def test_icon():
    """Test the custom icon"""
    root = tk.Tk()
    root.title("Icon Test - Customer Management System")
    root.geometry("400x300")
    
    # Test icon loading
    try:
        if os.path.exists("app_icon.ico"):
            print("✅ Found app_icon.ico")
            root.iconbitmap("app_icon.ico")
            print("✅ iconbitmap() set successfully")
        else:
            print("❌ app_icon.ico not found")
            
        if os.path.exists("app_icon_small.png"):
            print("✅ Found app_icon_small.png")
            try:
                icon_photo = tk.PhotoImage(file="app_icon_small.png")
                root.iconphoto(True, icon_photo)
                root.icon_photo = icon_photo  # Keep reference
                print("✅ iconphoto() set successfully with small PNG")
            except Exception as e:
                print(f"❌ Small PNG iconphoto failed: {e}")
        elif os.path.exists("app_icon.png"):
            print("✅ Found app_icon.png")
            try:
                icon_photo = tk.PhotoImage(file="app_icon.png")
                root.iconphoto(True, icon_photo)
                root.icon_photo = icon_photo  # Keep reference
                print("✅ iconphoto() set successfully with PNG")
            except Exception as e:
                print(f"❌ PNG iconphoto failed: {e}")
        else:
            print("ℹ️ No PNG files found")
            
    except Exception as e:
        print(f"❌ Icon loading failed: {e}")
    
    # Add some content
    label = tk.Label(root, text="Icon Test Window\n\nCheck the title bar and taskbar\nfor the custom icon!", 
                    font=("Arial", 14), pady=50)
    label.pack()
    
    # Instructions
    instructions = tk.Label(root, text="If you see the Python icon in the taskbar,\nrun 'python create_icon.py' first,\nthen restart this test.", 
                          font=("Arial", 10), fg="blue")
    instructions.pack(pady=20)
    
    # Close button
    close_btn = tk.Button(root, text="Close Test", command=root.destroy)
    close_btn.pack(pady=20)
    
    print("\n🔍 Icon Test Instructions:")
    print("1. Check the window title bar icon")
    print("2. Check the taskbar icon")
    print("3. Both should show the custom CMS icon")
    print("4. If not, run: python create_icon.py")
    
    root.mainloop()

if __name__ == "__main__":
    print("Testing custom icon...")
    test_icon()
