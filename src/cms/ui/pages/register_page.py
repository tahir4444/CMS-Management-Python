"""Register page component"""

import tkinter as tk
from tkinter import ttk


class RegisterPage:
    """Register page for the application"""
    
    def __init__(self, app):
        self.app = app
        self.main_frame = app.main_frame
    
    def show(self):
        """Show the register page"""
        # Clear main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        # Configure main frame for responsive layout
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)
        
        # Create responsive container
        container_frame = ttk.Frame(self.main_frame)
        container_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        container_frame.grid_columnconfigure(0, weight=1)
        container_frame.grid_rowconfigure(0, weight=1)
        
        # Create responsive card frame
        card_frame = ttk.Frame(container_frame, style="Card.TFrame")
        card_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        card_frame.grid_columnconfigure(0, weight=1)
        
        # Responsive padding
        def get_responsive_padding():
            width = self.app.root.winfo_width()
            if width < 900:
                return 20, 15
            elif width < 1200:
                return 30, 20
            else:
                return 40, 25
        
        pad_x, pad_y = get_responsive_padding()
        
        # App Logo/Title Section
        logo_frame = ttk.Frame(card_frame)
        logo_frame.grid(row=0, column=0, sticky="ew", pady=(pad_y, pad_y//2))
        logo_frame.grid_columnconfigure(0, weight=1)
        
        # Responsive title font
        title_font = ("Segoe UI", 16, "bold") if self.app.root.winfo_width() < 900 else ("Segoe UI", 18, "bold")
        app_title = ttk.Label(logo_frame, text="CUSTOMER MANAGEMENT SYSTEM", 
                             font=title_font, foreground="#2c3e50")
        app_title.grid(row=0, column=0, pady=(0, 5))
        
        subtitle_font = ("Segoe UI", 9) if self.app.root.winfo_width() < 900 else ("Segoe UI", 10)
        subtitle = ttk.Label(logo_frame, text="Create New Account", 
                            font=subtitle_font, foreground="#7f8c8d")
        subtitle.grid(row=1, column=0, pady=(0, pad_y))
        
        # Registration Form Section with responsive layout
        form_frame = ttk.Frame(card_frame)
        form_frame.grid(row=1, column=0, sticky="ew", padx=pad_x, pady=(0, pad_y))
        form_frame.grid_columnconfigure(0, weight=1)
        form_frame.grid_columnconfigure(1, weight=1)
        
        # Welcome message
        welcome_font = ("Segoe UI", 14, "bold") if self.app.root.winfo_width() < 900 else ("Segoe UI", 16, "bold")
        welcome_label = ttk.Label(form_frame, text="Join Our System", 
                                 font=welcome_font, foreground="#34495e")
        welcome_label.grid(row=0, column=0, columnspan=2, pady=(0, pad_y), sticky="w")
        
        # Responsive field layout - stack vertically on small screens
        if self.app.root.winfo_width() < 900:
            # Small screen: vertical layout
            self._create_vertical_registration_form(form_frame, pad_x, pad_y)
        else:
            # Large screen: two-column layout
            self._create_two_column_registration_form(form_frame, pad_x, pad_y)
        
        # Footer
        footer_frame = ttk.Frame(card_frame)
        footer_frame.grid(row=2, column=0, sticky="ew", pady=(0, pad_y//2))
        footer_frame.grid_columnconfigure(0, weight=1)
        
        footer_font = ("Segoe UI", 7) if self.app.root.winfo_width() < 900 else ("Segoe UI", 8)
        footer_text = ttk.Label(footer_frame, text="© 2024 Customer Management System. All rights reserved.", 
                               font=footer_font, foreground="#95a5a6")
        footer_text.grid(row=0, column=0)
        
        # Bind Enter key to register
        self.app.root.bind('<Return>', lambda e: self.register())
        
        # Focus on first name field
        self.first_name_entry.focus_set()
    
    def _create_vertical_registration_form(self, form_frame, pad_x, pad_y):
        """Create vertical layout for small screens"""
        field_label_font = ("Segoe UI", 9, "bold")
        entry_width = 30
        
        # First Name field
        first_name_frame = ttk.Frame(form_frame)
        first_name_frame.grid(row=1, column=0, sticky="ew", pady=(0, pad_y//2))
        first_name_frame.grid_columnconfigure(0, weight=1)
        
        first_name_label = ttk.Label(first_name_frame, text="First Name", 
                                    font=field_label_font, foreground="#2c3e50")
        first_name_label.grid(row=0, column=0, sticky="w", pady=(0, 8))
        
        self.first_name_entry = ttk.Entry(first_name_frame, font=("Segoe UI", 11), width=entry_width)
        self.first_name_entry.grid(row=1, column=0, sticky="ew", pady=(0, 5))
        
        # Last Name field
        last_name_frame = ttk.Frame(form_frame)
        last_name_frame.grid(row=2, column=0, sticky="ew", pady=(0, pad_y//2))
        last_name_frame.grid_columnconfigure(0, weight=1)
        
        last_name_label = ttk.Label(last_name_frame, text="Last Name", 
                                   font=field_label_font, foreground="#2c3e50")
        last_name_label.grid(row=0, column=0, sticky="w", pady=(0, 8))
        
        self.last_name_entry = ttk.Entry(last_name_frame, font=("Segoe UI", 11), width=entry_width)
        self.last_name_entry.grid(row=1, column=0, sticky="ew", pady=(0, 5))
        
        # Email field
        email_frame = ttk.Frame(form_frame)
        email_frame.grid(row=3, column=0, sticky="ew", pady=(0, pad_y//2))
        email_frame.grid_columnconfigure(0, weight=1)
        
        email_label = ttk.Label(email_frame, text="Email Address", 
                               font=field_label_font, foreground="#2c3e50")
        email_label.grid(row=0, column=0, sticky="w", pady=(0, 8))
        
        self.email_entry = ttk.Entry(email_frame, font=("Segoe UI", 11), width=entry_width)
        self.email_entry.grid(row=1, column=0, sticky="ew", pady=(0, 5))
        
        # Phone field
        phone_frame = ttk.Frame(form_frame)
        phone_frame.grid(row=4, column=0, sticky="ew", pady=(0, pad_y//2))
        phone_frame.grid_columnconfigure(0, weight=1)
        
        phone_label = ttk.Label(phone_frame, text="Phone Number", 
                               font=field_label_font, foreground="#2c3e50")
        phone_label.grid(row=0, column=0, sticky="w", pady=(0, 8))
        
        self.phone_entry = ttk.Entry(phone_frame, font=("Segoe UI", 11), width=entry_width)
        self.phone_entry.grid(row=1, column=0, sticky="ew", pady=(0, 5))
        
        # Password field
        password_frame = ttk.Frame(form_frame)
        password_frame.grid(row=5, column=0, sticky="ew", pady=(0, pad_y//2))
        password_frame.grid_columnconfigure(0, weight=1)
        
        password_label = ttk.Label(password_frame, text="Password", 
                                  font=field_label_font, foreground="#2c3e50")
        password_label.grid(row=0, column=0, sticky="w", pady=(0, 8))
        
        self.password_entry = ttk.Entry(password_frame, show="●", font=("Segoe UI", 11), width=entry_width)
        self.password_entry.grid(row=1, column=0, sticky="ew", pady=(0, 5))
        
        # Confirm Password field
        confirm_password_frame = ttk.Frame(form_frame)
        confirm_password_frame.grid(row=6, column=0, sticky="ew", pady=(0, pad_y//2))
        confirm_password_frame.grid_columnconfigure(0, weight=1)
        
        confirm_password_label = ttk.Label(confirm_password_frame, text="Confirm Password", 
                                         font=field_label_font, foreground="#2c3e50")
        confirm_password_label.grid(row=0, column=0, sticky="w", pady=(0, 8))
        
        self.confirm_password_entry = ttk.Entry(confirm_password_frame, show="●", font=("Segoe UI", 11), width=entry_width)
        self.confirm_password_entry.grid(row=1, column=0, sticky="ew", pady=(0, 5))
        
        # Terms and conditions checkbox
        terms_frame = ttk.Frame(form_frame)
        terms_frame.grid(row=7, column=0, sticky="ew", pady=(0, pad_y//2))
        
        terms_var = tk.BooleanVar()
        terms_check = ttk.Checkbutton(terms_frame, text="I agree to the Terms and Conditions", 
                                     variable=terms_var, style="Checkbutton.TCheckbutton")
        terms_check.grid(row=0, column=0, sticky="w")
        
        # Register button
        button_frame = ttk.Frame(form_frame)
        button_frame.grid(row=8, column=0, sticky="ew", pady=(0, pad_y//2))
        button_frame.grid_columnconfigure(0, weight=1)
        
        button_width = 18 if self.app.root.winfo_width() < 900 else 20
        register_btn = ttk.Button(button_frame, text="CREATE ACCOUNT", command=self.register, 
                                 style="Primary.TButton", width=button_width)
        register_btn.grid(row=0, column=0, pady=10)
        
        # Divider and login link
        self._create_form_footer(form_frame, 9, pad_y)
    
    def _create_two_column_registration_form(self, form_frame, pad_x, pad_y):
        """Create two-column layout for large screens"""
        field_label_font = ("Segoe UI", 10, "bold")
        entry_width = 25
        
        # First Name field
        first_name_frame = ttk.Frame(form_frame)
        first_name_frame.grid(row=1, column=0, sticky="ew", pady=(0, pad_y//2), padx=(0, 10))
        first_name_frame.grid_columnconfigure(0, weight=1)
        
        first_name_label = ttk.Label(first_name_frame, text="First Name", 
                                    font=field_label_font, foreground="#2c3e50")
        first_name_label.grid(row=0, column=0, sticky="w", pady=(0, 8))
        
        self.first_name_entry = ttk.Entry(first_name_frame, font=("Segoe UI", 11), width=entry_width)
        self.first_name_entry.grid(row=1, column=0, sticky="ew", pady=(0, 5))
        
        # Last Name field
        last_name_frame = ttk.Frame(form_frame)
        last_name_frame.grid(row=1, column=1, sticky="ew", pady=(0, pad_y//2), padx=(10, 0))
        last_name_frame.grid_columnconfigure(0, weight=1)
        
        last_name_label = ttk.Label(last_name_frame, text="Last Name", 
                                   font=field_label_font, foreground="#2c3e50")
        last_name_label.grid(row=0, column=0, sticky="w", pady=(0, 8))
        
        self.last_name_entry = ttk.Entry(last_name_frame, font=("Segoe UI", 11), width=entry_width)
        self.last_name_entry.grid(row=1, column=0, sticky="ew", pady=(0, 5))
        
        # Email field
        email_frame = ttk.Frame(form_frame)
        email_frame.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(0, pad_y//2))
        email_frame.grid_columnconfigure(0, weight=1)
        
        email_label = ttk.Label(email_frame, text="Email Address", 
                               font=field_label_font, foreground="#2c3e50")
        email_label.grid(row=0, column=0, sticky="w", pady=(0, 8))
        
        self.email_entry = ttk.Entry(email_frame, font=("Segoe UI", 11), width=35)
        self.email_entry.grid(row=1, column=0, sticky="ew", pady=(0, 5))
        
        # Phone field
        phone_frame = ttk.Frame(form_frame)
        phone_frame.grid(row=3, column=0, columnspan=2, sticky="ew", pady=(0, pad_y//2))
        phone_frame.grid_columnconfigure(0, weight=1)
        
        phone_label = ttk.Label(phone_frame, text="Phone Number", 
                               font=field_label_font, foreground="#2c3e50")
        phone_label.grid(row=0, column=0, sticky="w", pady=(0, 8))
        
        self.phone_entry = ttk.Entry(phone_frame, font=("Segoe UI", 11), width=35)
        self.phone_entry.grid(row=1, column=0, sticky="ew", pady=(0, 5))
        
        # Password field
        password_frame = ttk.Frame(form_frame)
        password_frame.grid(row=4, column=0, sticky="ew", pady=(0, pad_y//2), padx=(0, 10))
        password_frame.grid_columnconfigure(0, weight=1)
        
        password_label = ttk.Label(password_frame, text="Password", 
                                  font=field_label_font, foreground="#2c3e50")
        password_label.grid(row=0, column=0, sticky="w", pady=(0, 8))
        
        self.password_entry = ttk.Entry(password_frame, show="●", font=("Segoe UI", 11), width=entry_width)
        self.password_entry.grid(row=1, column=0, sticky="ew", pady=(0, 5))
        
        # Confirm Password field
        confirm_password_frame = ttk.Frame(form_frame)
        confirm_password_frame.grid(row=4, column=1, sticky="ew", pady=(0, pad_y//2), padx=(10, 0))
        confirm_password_frame.grid_columnconfigure(0, weight=1)
        
        confirm_password_label = ttk.Label(confirm_password_frame, text="Confirm Password", 
                                         font=field_label_font, foreground="#2c3e50")
        confirm_password_label.grid(row=0, column=0, sticky="w", pady=(0, 8))
        
        self.confirm_password_entry = ttk.Entry(confirm_password_frame, show="●", font=("Segoe UI", 11), width=entry_width)
        self.confirm_password_entry.grid(row=1, column=0, sticky="ew", pady=(0, 5))
        
        # Terms and conditions checkbox
        terms_frame = ttk.Frame(form_frame)
        terms_frame.grid(row=5, column=0, columnspan=2, sticky="ew", pady=(0, pad_y//2))
        
        terms_var = tk.BooleanVar()
        terms_check = ttk.Checkbutton(terms_frame, text="I agree to the Terms and Conditions", 
                                     variable=terms_var, style="Checkbutton.TCheckbutton")
        terms_check.grid(row=0, column=0, sticky="w")
        
        # Register button
        button_frame = ttk.Frame(form_frame)
        button_frame.grid(row=6, column=0, columnspan=2, sticky="ew", pady=(0, pad_y//2))
        button_frame.grid_columnconfigure(0, weight=1)
        
        button_width = 18 if self.app.root.winfo_width() < 900 else 20
        register_btn = ttk.Button(button_frame, text="CREATE ACCOUNT", command=self.register, 
                                 style="Primary.TButton", width=button_width)
        register_btn.grid(row=0, column=0, pady=10)
        
        # Divider and login link
        self._create_form_footer(form_frame, 7, pad_y)
    
    def _create_form_footer(self, form_frame, row, pad_y):
        """Create the footer section with divider and login link"""
        # Divider line
        divider_frame = ttk.Frame(form_frame)
        divider_frame.grid(row=row, column=0, columnspan=2, sticky="ew", pady=(0, pad_y//2))
        divider_frame.grid_columnconfigure(1, weight=1)
        
        divider_line1 = tk.Frame(divider_frame, height=1, background="#e0e0e0")
        divider_line1.grid(row=0, column=0, sticky="ew", padx=(0, 15))
        
        divider_text = ttk.Label(divider_frame, text="or", font=("Segoe UI", 9), foreground="#95a5a6")
        divider_text.grid(row=0, column=1)
        
        divider_line2 = tk.Frame(divider_frame, height=1, background="#e0e0e0")
        divider_line2.grid(row=0, column=2, sticky="ew", padx=(15, 0))
        
        # Login link
        login_frame = ttk.Frame(form_frame)
        login_frame.grid(row=row+1, column=0, columnspan=2, sticky="ew")
        login_frame.grid_columnconfigure(0, weight=1)
        
        link_font = ("Segoe UI", 9) if self.app.root.winfo_width() < 900 else ("Segoe UI", 10)
        login_text = ttk.Label(login_frame, text="Already have an account?", 
                              font=link_font, foreground="#7f8c8d")
        login_text.grid(row=0, column=0, pady=(0, 5))
        
        login_link = ttk.Label(login_frame, text="Sign In Here", 
                              foreground="#3498db", cursor="hand2", 
                              font=link_font + ("bold",))
        login_link.grid(row=1, column=0, pady=(0, pad_y//2))
        login_link.bind("<Button-1>", lambda e: self.app.show_login_page())
    
    def register(self):
        """Handle registration"""
        # Get form data
        first_name = self.first_name_entry.get().strip()
        last_name = self.last_name_entry.get().strip()
        email = self.email_entry.get().strip()
        phone = self.phone_entry.get().strip()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        
        # Validate required fields
        if not all([first_name, last_name, email, phone, password, confirm_password]):
            self.app.message_box.show_error("Error", "Please fill in all required fields!")
            return
        
        # Validate email format
        import re
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            self.app.message_box.show_error("Error", "Please enter a valid email address!")
            return
        
        # Validate password match
        if password != confirm_password:
            self.app.message_box.show_error("Error", "Passwords do not match!")
            return
        
        # Validate password length
        if len(password) < 6:
            self.app.message_box.show_error("Error", "Password must be at least 6 characters long!")
            return
        
        try:
            # Check if email already exists
            if self.app.database_service.email_exists(email):
                self.app.message_box.show_error("Error", "Email address already registered!")
                return
            
            # Register user
            user_id = self.app.auth_service.register_user(first_name, last_name, email, phone, password)
            
            if user_id:
                # Send welcome email
                try:
                    welcome_sent = self.app.email_service.send_welcome_email(
                        email, 
                        f"{first_name} {last_name}", 
                        user_id
                    )
                    
                    if welcome_sent:
                        self.app.message_box.show_info("Success", 
                            f"Account created successfully! Welcome, {first_name} {last_name}!\n\nA welcome email has been sent to {email}.")
                    else:
                        self.app.message_box.show_info("Success", 
                            f"Account created successfully! Welcome, {first_name} {last_name}!\n\nNote: Welcome email could not be sent.")
                        
                except Exception as email_error:
                    print(f"Email error: {email_error}")
                    self.app.message_box.show_info("Success", 
                        f"Account created successfully! Welcome, {first_name} {last_name}!")
                
                # Navigate to login page
                self.app.show_login_page()
            else:
                self.app.message_box.show_error("Error", "Failed to create account. Please try again.")
                
        except Exception as e:
            self.app.message_box.show_error("Error", f"Registration failed: {str(e)}")
