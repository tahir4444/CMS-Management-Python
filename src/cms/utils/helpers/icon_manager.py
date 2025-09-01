"""Icon manager for handling application icons"""

import os
import tkinter as tk


class IconManager:
    """Manages application icons"""
    
    def __init__(self, root):
        self.root = root
        self.setup_icons()
    
    def setup_icons(self):
        """Setup application icons"""
        try:
            # Try to load the custom icon
            if os.path.exists("app_icon.ico"):
                # Set icon for the window
                self.root.iconbitmap("app_icon.ico")
                
                # Also set iconphoto for taskbar (Windows specific)
                try:
                    # Try small PNG first for better tkinter compatibility
                    if os.path.exists("app_icon_small.png"):
                        icon_photo = tk.PhotoImage(file="app_icon_small.png")
                        print("✅ Using small PNG for taskbar")
                    elif os.path.exists("app_icon.png"):
                        icon_photo = tk.PhotoImage(file="app_icon.png")
                        print("✅ Using PNG for taskbar")
                    else:
                        # Fallback to ICO
                        icon_photo = tk.PhotoImage(file="app_icon.ico")
                        print("✅ Using ICO for taskbar")
                    
                    self.root.iconphoto(True, icon_photo)
                    # Keep reference to prevent garbage collection
                    self.icon_photo = icon_photo
                    print("✅ Custom icon loaded successfully for window and taskbar!")
                except Exception as photo_error:
                    # If PhotoImage fails, try alternative method
                    print(f"⚠️ PhotoImage failed: {str(photo_error)}")
                    blank_photo = tk.PhotoImage(width=1, height=1)
                    self.root.iconphoto(True, blank_photo)
                    self.icon_photo = blank_photo
                    print("ℹ️ Using blank icon for taskbar")
            else:
                # Create a minimal blank photo to replace the default icon
                blank_photo = tk.PhotoImage(width=1, height=1)
                self.root.iconphoto(True, blank_photo)
                self.icon_photo = blank_photo
                print("ℹ️ Using blank icon (run create_icon.py to create custom icon)")
        except Exception as e:
            # If icon loading fails, just continue without it
            print(f"⚠️ Icon loading failed: {str(e)}")
            pass
