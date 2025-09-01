"""Custom message box dialog"""

import tkinter as tk
from tkinter import ttk


class CustomMessageBox:
    """Custom message box for the application"""
    
    def __init__(self, parent):
        self.parent = parent
    
    def show_error(self, title, message):
        """Show error dialog"""
        dialog = tk.Toplevel(self.parent)
        dialog.title(title)
        dialog.geometry("350x180")
        dialog.resizable(False, False)
        dialog.transient(self.parent)
        dialog.grab_set()
        
        # Center the dialog
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - (350 // 2)
        y = (dialog.winfo_screenheight() // 2) - (180 // 2)
        dialog.geometry(f"350x180+{x}+{y}")
        
        # Create main frame
        main_frame = ttk.Frame(dialog, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Error title
        title_label = ttk.Label(main_frame, text=title, font=("Arial", 12, "bold"), foreground="red")
        title_label.pack(pady=(0, 15))
        
        # Message
        msg_label = ttk.Label(main_frame, text=message, wraplength=280, justify="center", font=("Arial", 10))
        msg_label.pack(pady=(0, 20))
        
        # OK button
        ok_btn = ttk.Button(main_frame, text="OK", command=dialog.destroy, width=10)
        ok_btn.pack()
        
        dialog.focus_set()
        dialog.bind('<Return>', lambda e: dialog.destroy())
        dialog.bind('<Escape>', lambda e: dialog.destroy())
        
        dialog.wait_window()
    
    def show_info(self, title, message):
        """Show info dialog"""
        dialog = tk.Toplevel(self.parent)
        dialog.title(title)
        dialog.geometry("350x180")
        dialog.resizable(False, False)
        dialog.transient(self.parent)
        dialog.grab_set()
        
        # Center the dialog
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - (350 // 2)
        y = (dialog.winfo_screenheight() // 2) - (180 // 2)
        dialog.geometry(f"350x180+{x}+{y}")
        
        # Create main frame
        main_frame = ttk.Frame(dialog, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Info title
        title_label = ttk.Label(main_frame, text=title, font=("Arial", 12, "bold"), foreground="blue")
        title_label.pack(pady=(0, 15))
        
        # Message
        msg_label = ttk.Label(main_frame, text=message, wraplength=280, justify="center", font=("Arial", 10))
        msg_label.pack(pady=(0, 20))
        
        # OK button
        ok_btn = ttk.Button(main_frame, text="OK", command=dialog.destroy, width=10)
        ok_btn.pack()
        
        dialog.focus_set()
        dialog.bind('<Return>', lambda e: dialog.destroy())
        dialog.bind('<Escape>', lambda e: dialog.destroy())
        
        dialog.wait_window()
    
    def show_confirm(self, title, message):
        """Show confirmation dialog and return True/False"""
        result = [False]  # Use list to store result
        
        dialog = tk.Toplevel(self.parent)
        dialog.title(title)
        dialog.geometry("400x200")
        dialog.resizable(False, False)
        dialog.transient(self.parent)
        dialog.grab_set()
        
        # Center the dialog
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - (400 // 2)
        y = (dialog.winfo_screenheight() // 2) - (200 // 2)
        dialog.geometry(f"400x200+{x}+{y}")
        
        # Create main frame
        main_frame = ttk.Frame(dialog, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Confirm title
        title_label = ttk.Label(main_frame, text=title, font=("Arial", 12, "bold"), foreground="orange")
        title_label.pack(pady=(0, 15))
        
        # Message
        msg_label = ttk.Label(main_frame, text=message, wraplength=320, justify="center", font=("Arial", 10))
        msg_label.pack(pady=(0, 20))
        
        # Buttons frame
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.pack()
        
        def on_yes():
            result[0] = True
            dialog.destroy()
        
        def on_no():
            result[0] = False
            dialog.destroy()
        
        # Yes button
        yes_btn = ttk.Button(buttons_frame, text="Yes", command=on_yes, width=8)
        yes_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # No button
        no_btn = ttk.Button(buttons_frame, text="No", command=on_no, width=8)
        no_btn.pack(side=tk.LEFT)
        
        dialog.focus_set()
        dialog.bind('<Return>', lambda e: on_yes())
        dialog.bind('<Escape>', lambda e: on_no())
        
        dialog.wait_window()
        return result[0]
