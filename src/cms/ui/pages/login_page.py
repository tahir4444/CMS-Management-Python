"""Login page component"""

import tkinter as tk
from tkinter import ttk


class LoginPage:
    """Login page for the application"""
    
    def __init__(self, app):
        self.app = app
        self.main_frame = app.main_frame
    
    def show(self):
        """Show the login page"""
        # Clear main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        # Configure main frame for professional layout
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)
        
        # Create professional container with gradient-like effect
        container_frame = ttk.Frame(self.main_frame, style="Professional.TFrame")
        container_frame.grid(row=0, column=0, sticky="nsew", padx=40, pady=40)
        container_frame.grid_columnconfigure(0, weight=1)
        container_frame.grid_rowconfigure(0, weight=1)
        
        # Create professional card frame with shadow effect
        card_frame = ttk.Frame(container_frame, style="Professional.TFrame")
        card_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        card_frame.grid_columnconfigure(0, weight=1)
        
        # Add professional padding and spacing
        pad_x, pad_y = 40, 30
        
        # Professional header section with logo area
        header_frame = ttk.Frame(card_frame, style="Professional.TFrame")
        header_frame.grid(row=0, column=0, sticky="ew", pady=(pad_y, pad_y//2))
        header_frame.grid_columnconfigure(0, weight=1)
        
        # Professional app title with modern typography
        app_title = ttk.Label(header_frame, text="Enterprise CMS", 
                             style="Title.TLabel")
        app_title.grid(row=0, column=0, pady=(0, 8))
        
        # Professional subtitle
        subtitle = ttk.Label(header_frame, text="Customer Management System", 
                            style="Subtitle.TLabel")
        subtitle.grid(row=1, column=0, pady=(0, 5))
        
        # Professional tagline
        tagline = ttk.Label(header_frame, text="Secure • Reliable • Professional", 
                           style="Caption.TLabel")
        tagline.grid(row=2, column=0, pady=(0, pad_y))
        
        # Professional form section
        form_frame = ttk.Frame(card_frame, style="Professional.TFrame")
        form_frame.grid(row=1, column=0, sticky="ew", padx=pad_x, pady=(0, pad_y))
        form_frame.grid_columnconfigure(0, weight=1)
        
        # Professional welcome message
        welcome_label = ttk.Label(form_frame, text="Welcome back to your dashboard", 
                                 style="Heading.TLabel")
        welcome_label.grid(row=0, column=0, pady=(0, pad_y), sticky="w")
        
        # Professional email field
        email_frame = ttk.Frame(form_frame, style="Professional.TFrame")
        email_frame.grid(row=1, column=0, sticky="ew", pady=(0, 20))
        email_frame.grid_columnconfigure(0, weight=1)
        
        email_label = ttk.Label(email_frame, text="Email Address", 
                               style="Body.TLabel")
        email_label.grid(row=0, column=0, sticky="w", pady=(0, 8))
        
        # Professional entry with modern styling
        self.email_entry = ttk.Entry(email_frame, style="Professional.TEntry", 
                                    font=("Inter", 14), width=35)
        self.email_entry.grid(row=1, column=0, sticky="ew", pady=(0, 5))
        
        # Professional password field
        password_frame = ttk.Frame(form_frame, style="Professional.TFrame")
        password_frame.grid(row=2, column=0, sticky="ew", pady=(0, 20))
        password_frame.grid_columnconfigure(0, weight=1)
        
        password_label = ttk.Label(password_frame, text="Password", 
                                  style="Body.TLabel")
        password_label.grid(row=0, column=0, sticky="w", pady=(0, 8))
        
        self.password_entry = ttk.Entry(password_frame, show="●", 
                                      style="Professional.TEntry",
                                      font=("Inter", 14), width=35)
        self.password_entry.grid(row=1, column=0, sticky="ew", pady=(0, 5))
        
        # Professional options row
        options_frame = ttk.Frame(form_frame, style="Professional.TFrame")
        options_frame.grid(row=3, column=0, sticky="ew", pady=(0, 25))
        options_frame.grid_columnconfigure(0, weight=1)
        options_frame.grid_columnconfigure(1, weight=1)
        
        # Professional checkbox
        self.remember_var = tk.BooleanVar()
        remember_check = ttk.Checkbutton(options_frame, text="Keep me signed in", 
                                       variable=self.remember_var, style="Professional.TCheckbutton")
        remember_check.grid(row=0, column=0, sticky="w")
        
        # Professional forgot password link
        forgot_link = ttk.Label(options_frame, text="Forgot your password?", 
                               foreground=self.app.style_manager.colors['primary'], cursor="hand2", 
                               style="Caption.TLabel")
        forgot_link.grid(row=0, column=1, sticky="e")
        forgot_link.bind("<Button-1>", lambda e: self.show_forgot_password())
        
        # Professional login button
        button_frame = ttk.Frame(form_frame, style="Professional.TFrame")
        button_frame.grid(row=4, column=0, sticky="ew", pady=(0, 25))
        button_frame.grid_columnconfigure(0, weight=1)
        
        login_btn = ttk.Button(button_frame, text="Sign In to Dashboard", 
                              command=self.login, 
                              style="Primary.TButton", width=30)
        login_btn.grid(row=0, column=0, pady=10)
        
        # Professional divider
        divider_frame = ttk.Frame(form_frame, style="Professional.TFrame")
        divider_frame.grid(row=5, column=0, sticky="ew", pady=(0, 25))
        divider_frame.grid_columnconfigure(1, weight=1)
        
        # Professional divider line
        divider_line1 = tk.Frame(divider_frame, height=1, 
                                background=self.app.style_manager.colors['border'])
        divider_line1.grid(row=0, column=0, sticky="ew", padx=(0, 20))
        
        divider_text = ttk.Label(divider_frame, text="or continue with", 
                                style="Caption.TLabel")
        divider_text.grid(row=0, column=1)
        
        divider_line2 = tk.Frame(divider_frame, height=1, 
                                background=self.app.style_manager.colors['border'])
        divider_line2.grid(row=0, column=2, sticky="ew", padx=(20, 0))
        
        # Professional registration section
        register_frame = ttk.Frame(form_frame, style="Professional.TFrame")
        register_frame.grid(row=6, column=0, sticky="ew")
        register_frame.grid_columnconfigure(0, weight=1)
        
        register_text = ttk.Label(register_frame, text="New to Enterprise CMS?", 
                                 style="Body.TLabel")
        register_text.grid(row=0, column=0, pady=(0, 8))
        
        register_link = ttk.Label(register_frame, text="Create your account", 
                                 foreground=self.app.style_manager.colors['primary'], cursor="hand2", 
                                 style="Body.TLabel")
        register_link.grid(row=1, column=0, pady=(0, 10))
        register_link.bind("<Button-1>", lambda e: self.app.show_register_page())
        
        # Professional footer
        footer_frame = ttk.Frame(card_frame, style="Professional.TFrame")
        footer_frame.grid(row=2, column=0, sticky="ew", pady=(pad_y, 0))
        footer_frame.grid_columnconfigure(0, weight=1)
        
        footer_text = ttk.Label(footer_frame, 
                               text="© 2024 Enterprise CMS. Enterprise-grade customer management.", 
                               style="Caption.TLabel")
        footer_text.grid(row=0, column=0)
        
        # Professional security note
        security_note = ttk.Label(footer_frame, 
                                 text="🔒 Your data is protected with enterprise-grade security", 
                                 style="Caption.TLabel")
        security_note.grid(row=1, column=0, pady=(5, 0))
        
        # Bind Enter key to login
        self.app.root.bind('<Return>', lambda e: self.login())
        
        # Load saved credentials if available
        saved_email, saved_password = self.app.auth_service.load_saved_credentials()
        if saved_email and saved_password:
            self.email_entry.insert(0, saved_email)
            self.password_entry.insert(0, saved_password)
            self.remember_var.set(True)
        
        # Focus on email field
        self.email_entry.focus_set()
    
    def show_forgot_password(self):
        """Show forgot password dialog"""
        # Create professional forgot password dialog
        dialog = tk.Toplevel(self.app.root)
        dialog.title("Password Reset - Enterprise CMS")
        dialog.geometry("500x650")
        dialog.resizable(False, False)
        dialog.transient(self.app.root)
        dialog.grab_set()
        
        # Set dialog icon
        try:
            dialog.iconbitmap("assets/icons/app_icon.ico")
        except:
            pass
        
        # Center the dialog
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - (500 // 2)
        y = (dialog.winfo_screenheight() // 2) - (650 // 2)
        dialog.geometry(f"500x650+{x}+{y}")
        
        # Create main container with gradient-like effect
        main_container = ttk.Frame(dialog, style="Professional.TFrame")
        main_container.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
        main_container.grid_columnconfigure(0, weight=1)
        main_container.grid_rowconfigure(1, weight=1)
        
        # Professional header section with background
        header_frame = ttk.Frame(main_container, style="Professional.TFrame")
        header_frame.grid(row=0, column=0, sticky="ew", padx=0, pady=0)
        header_frame.grid_columnconfigure(0, weight=1)
        
        # Professional title with icon
        title_frame = ttk.Frame(header_frame, style="Professional.TFrame")
        title_frame.grid(row=0, column=0, pady=(20, 8))
        title_frame.grid_columnconfigure(1, weight=1)
        
        # Lock icon
        lock_icon = ttk.Label(title_frame, text="🔐", font=("Segoe UI", 20))
        lock_icon.grid(row=0, column=0, padx=(0, 12))
        
        # Title text
        title_label = ttk.Label(title_frame, text="Password Reset", 
                               style="Title.TLabel", font=("Segoe UI", 18, "bold"))
        title_label.grid(row=0, column=1, sticky="w")
        
        # Subtitle
        subtitle_label = ttk.Label(header_frame, text="Secure Account Recovery", 
                                  style="Subtitle.TLabel", font=("Segoe UI", 11))
        subtitle_label.grid(row=1, column=0, pady=(0, 15))
        
        # Main content area
        content_frame = ttk.Frame(main_container, style="Professional.TFrame")
        content_frame.grid(row=1, column=0, sticky="nsew", padx=30, pady=(0, 20))
        content_frame.grid_columnconfigure(0, weight=1)
        
        # Professional instructions with better formatting
        instructions_frame = ttk.Frame(content_frame, style="Professional.TFrame")
        instructions_frame.grid(row=0, column=0, sticky="ew", pady=(0, 20))
        instructions_frame.grid_columnconfigure(0, weight=1)
        
        instructions_title = ttk.Label(instructions_frame, text="How it works:", 
                                      style="Heading.TLabel", font=("Segoe UI", 11, "bold"))
        instructions_title.grid(row=0, column=0, pady=(0, 8), sticky="w")
        
        instructions_text = ttk.Label(instructions_frame, 
                                     text="1. Enter your registered email address\n2. We'll send you a secure temporary password\n3. Use the temporary password to log in\n4. Change your password immediately after login",
                                     style="Body.TLabel", font=("Segoe UI", 9), 
                                     wraplength=400, justify="left")
        instructions_text.grid(row=1, column=0, pady=(0, 15), sticky="w")
        
        # Professional email input section with enhanced styling
        email_section = ttk.Frame(content_frame, style="Professional.TFrame")
        email_section.grid(row=1, column=0, sticky="ew", pady=(0, 15))
        email_section.grid_columnconfigure(0, weight=1)
        
        # Email label with icon
        email_label_frame = ttk.Frame(email_section, style="Professional.TFrame")
        email_label_frame.grid(row=0, column=0, sticky="w", pady=(0, 6))
        
        email_icon = ttk.Label(email_label_frame, text="📧", font=("Segoe UI", 11))
        email_icon.grid(row=0, column=0, padx=(0, 6))
        
        email_label = ttk.Label(email_label_frame, text="Email Address", 
                               style="Body.TLabel", font=("Segoe UI", 10, "bold"))
        email_label.grid(row=0, column=1, sticky="w")
        
        # Email entry with enhanced styling
        email_entry = ttk.Entry(email_section, style="Professional.TEntry", 
                               font=("Segoe UI", 11), width=40)
        email_entry.grid(row=1, column=0, sticky="ew", pady=(0, 5))
        
        # Professional status label with better positioning
        status_frame = ttk.Frame(content_frame, style="Professional.TFrame")
        status_frame.grid(row=2, column=0, sticky="ew", pady=(0, 20))
        status_frame.grid_columnconfigure(0, weight=1)
        
        status_label = ttk.Label(status_frame, text="", 
                                style="Caption.TLabel", font=("Segoe UI", 9), 
                                wraplength=400, justify="center")
        status_label.grid(row=0, column=0, pady=5)
        
        # Professional buttons section
        buttons_section = ttk.Frame(content_frame, style="Professional.TFrame")
        buttons_section.grid(row=3, column=0, sticky="ew", pady=(0, 15))
        buttons_section.grid_columnconfigure(0, weight=1)
        buttons_section.grid_columnconfigure(1, weight=1)
        
        def reset_password():
            """Handle password reset"""
            email = email_entry.get().strip()
            
            if not email:
                status_label.config(text="❌ Please enter your email address", 
                                  foreground=self.app.style_manager.colors['error'])
                return
            
            # Validate email format
            import re
            email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.match(email_pattern, email):
                status_label.config(text="❌ Please enter a valid email address", 
                                  foreground=self.app.style_manager.colors['error'])
                return
            
            # Check if email exists in database
            if not self.app.database_service.email_exists(email):
                status_label.config(text="❌ Email address not found in our system", 
                                  foreground=self.app.style_manager.colors['error'])
                return
            
            try:
                # Get user info for email
                user_info = self.app.database_service.get_customer_by_email(email)
                if not user_info:
                    status_label.config(text="❌ User not found", 
                                      foreground=self.app.style_manager.colors['error'])
                    return
                
                # Generate temporary password
                temp_password = self.app.auth_service.reset_password(email)
                
                # Send email
                user_name = f"{user_info[1]} {user_info[2]}"
                email_sent = self.app.email_service.send_password_reset_email(email, temp_password, user_name)
                
                if email_sent:
                    status_label.config(text="✅ Password reset email sent successfully! Check your inbox.", 
                                      foreground=self.app.style_manager.colors['success'])
                    # Clear email field
                    email_entry.delete(0, tk.END)
                else:
                    status_label.config(text="❌ Failed to send email. Please try again later.", 
                                      foreground=self.app.style_manager.colors['error'])
                    
            except Exception as e:
                status_label.config(text=f"❌ Error: {str(e)}", 
                                  foreground=self.app.style_manager.colors['error'])
        
        def cancel_reset():
            """Cancel password reset"""
            dialog.destroy()
        
        # Enhanced reset button
        reset_btn = ttk.Button(buttons_section, text="🔐 Reset Password", 
                              command=reset_password, 
                              style="Primary.TButton", width=20)
        reset_btn.grid(row=0, column=0, padx=(0, 10), pady=10)
        
        # Enhanced cancel button
        cancel_btn = ttk.Button(buttons_section, text="❌ Cancel", 
                               command=cancel_reset, 
                               style="Secondary.TButton", width=20)
        cancel_btn.grid(row=0, column=1, padx=(10, 0), pady=10)
        
        # Professional footer section
        footer_frame = ttk.Frame(main_container, style="Professional.TFrame")
        footer_frame.grid(row=2, column=0, sticky="ew", padx=30, pady=(0, 20))
        footer_frame.grid_columnconfigure(0, weight=1)
        
        # Security note
        security_note = ttk.Label(footer_frame, 
                                 text="🔒 Your security is our priority. Temporary passwords expire in 24 hours.",
                                 style="Caption.TLabel", font=("Segoe UI", 8), 
                                 wraplength=400, justify="center")
        security_note.grid(row=0, column=0, pady=(0, 8))
        
        # Help text
        help_text = ttk.Label(footer_frame, 
                             text="💡 Can't find the email? Check your spam folder or contact support.",
                             style="Caption.TLabel", font=("Segoe UI", 8), 
                             wraplength=400, justify="center")
        help_text.grid(row=1, column=0)
        
        # Focus on email field
        email_entry.focus_set()
        
        # Bind Enter key to reset password
        dialog.bind('<Return>', lambda e: reset_password())
        dialog.bind('<Escape>', lambda e: cancel_reset())
        
        # Make dialog modal
        dialog.focus_set()
        dialog.wait_window()
    
    def login(self):
        """Handle login"""
        email = self.email_entry.get().strip()
        password = self.password_entry.get()
        
        if not email or not password:
            self.app.message_box.show_error("Error", "Please enter both email and password!")
            return
        
        try:
            # Authenticate user
            user = self.app.auth_service.authenticate_user(email, password)
            
            if user:
                # Save credentials if "Keep me signed in" is checked
                if self.remember_var.get():
                    self.app.auth_service.save_credentials(email, password)
                
                # Show success message and navigate to dashboard
                self.app.message_box.show_info("Success", f"Welcome back, {user[1]} {user[2]}!")
                self.app.show_dashboard(user)
            else:
                self.app.message_box.show_error("Login Failed", "Invalid email or password. Please try again.")
                
        except Exception as e:
            self.app.message_box.show_error("Error", f"Login failed: {str(e)}")
