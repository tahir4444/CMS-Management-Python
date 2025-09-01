"""Dashboard page component"""

import tkinter as tk
from tkinter import ttk
import hashlib
from datetime import datetime


class DashboardPage:
    """Dashboard page for the application"""
    
    def __init__(self, app, user):
        self.app = app
        self.user = user
        self.main_frame = app.main_frame
    
    def show(self):
        """Show the dashboard page"""
        # Clear main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        # Configure main frame for professional layout
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)
        
        # Create professional container
        container_frame = ttk.Frame(self.main_frame, style="Professional.TFrame")
        container_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        container_frame.grid_columnconfigure(0, weight=1)
        container_frame.grid_rowconfigure(0, weight=1)
        
        # Create professional card frame
        card_frame = ttk.Frame(container_frame, style="Professional.TFrame")
        card_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        card_frame.grid_columnconfigure(0, weight=1)
        
        # Professional header section
        header_frame = ttk.Frame(card_frame, style="Professional.TFrame")
        header_frame.grid(row=0, column=0, sticky="ew", pady=(20, 30))
        header_frame.grid_columnconfigure(0, weight=1)
        
        # Professional welcome message
        welcome_label = ttk.Label(header_frame, text=f"Welcome back, {self.user[1]} {self.user[2]}!", 
                                style="Title.TLabel")
        welcome_label.grid(row=0, column=0, pady=(0, 10))
        
        # Professional subtitle
        subtitle = ttk.Label(header_frame, text="Your Enterprise CMS Dashboard", 
                           style="Subtitle.TLabel")
        subtitle.grid(row=1, column=0, pady=(0, 20))
        
        # Professional navigation section
        nav_frame = ttk.Frame(card_frame, style="Professional.TFrame")
        nav_frame.grid(row=1, column=0, sticky="ew", pady=(0, 30))
        nav_frame.grid_columnconfigure(0, weight=1)
        nav_frame.grid_columnconfigure(1, weight=1)
        nav_frame.grid_columnconfigure(2, weight=1)
        
        # Professional navigation buttons
        users_btn = ttk.Button(nav_frame, text="👥 Users Management", 
                              command=self.app.show_users_list, 
                              style="Primary.TButton", width=20)
        users_btn.grid(row=0, column=0, padx=10, pady=10)
        
        profile_btn = ttk.Button(nav_frame, text="👤 My Profile", 
                                command=self.show_profile, 
                                style="Secondary.TButton", width=20)
        profile_btn.grid(row=0, column=1, padx=10, pady=10)
        
        settings_btn = ttk.Button(nav_frame, text="⚙️ Settings", 
                                 command=self.show_settings, 
                                 style="Secondary.TButton", width=20)
        settings_btn.grid(row=0, column=2, padx=10, pady=10)
        
        # Professional dashboard content
        content_frame = ttk.Frame(card_frame, style="Professional.TFrame")
        content_frame.grid(row=2, column=0, sticky="ew", pady=(0, 30))
        content_frame.grid_columnconfigure(0, weight=1)
        content_frame.grid_columnconfigure(1, weight=1)
        
        # Professional stats cards
        stats_frame = ttk.Frame(content_frame, style="Professional.TFrame")
        stats_frame.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 20))
        stats_frame.grid_columnconfigure(0, weight=1)
        stats_frame.grid_columnconfigure(1, weight=1)
        stats_frame.grid_columnconfigure(2, weight=1)
        stats_frame.grid_columnconfigure(3, weight=1)
        
        # Professional stat cards with dynamic data
        total_users = self.app.database_service.get_customer_count()
        recent_registrations = self.app.database_service.get_recent_registrations_count(7)
        today_registrations = self.app.database_service.get_today_registrations_count()
        
        self._create_stat_card(stats_frame, "Total Users", f"{total_users:,}", "👥", 0)
        self._create_stat_card(stats_frame, "This Week", f"{recent_registrations}", "📈", 1)
        self._create_stat_card(stats_frame, "Today", f"{today_registrations}", "🆕", 2)
        self._create_stat_card(stats_frame, "System Status", "Online", "✅", 3)
        
        # Professional recent activity section
        activity_frame = ttk.Frame(content_frame, style="Professional.TFrame")
        activity_frame.grid(row=1, column=0, sticky="ew", pady=(0, 20))
        activity_frame.grid_columnconfigure(0, weight=1)
        
        activity_title = ttk.Label(activity_frame, text="Recent Activity", 
                                 style="Heading.TLabel")
        activity_title.grid(row=0, column=0, pady=(0, 15), sticky="w")
        
        # Professional activity list with dynamic data
        recent_activities = self.app.database_service.get_recent_activity(4)
        
        if recent_activities:
            for i, activity in enumerate(recent_activities):
                first_name, last_name, email, created_at = activity
                # Format the date
                try:
                    date_obj = datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S')
                    formatted_date = date_obj.strftime('%b %d, %H:%M')
                except:
                    formatted_date = created_at
                
                activity_text = f"🆕 {first_name} {last_name} ({email}) - {formatted_date}"
                activity_label = ttk.Label(activity_frame, text=activity_text, 
                                         style="Body.TLabel")
                activity_label.grid(row=i+1, column=0, pady=2, sticky="w")
        else:
            no_activity_label = ttk.Label(activity_frame, text="No recent activity", 
                                        style="Caption.TLabel", foreground="gray")
            no_activity_label.grid(row=1, column=0, pady=2, sticky="w")
        
        # Professional quick actions section
        actions_frame = ttk.Frame(content_frame, style="Professional.TFrame")
        actions_frame.grid(row=1, column=1, sticky="ew", padx=(20, 0))
        actions_frame.grid_columnconfigure(0, weight=1)
        
        actions_title = ttk.Label(actions_frame, text="Quick Actions", 
                                style="Heading.TLabel")
        actions_title.grid(row=0, column=0, pady=(0, 15), sticky="w")
        
        # Professional quick action buttons
        quick_actions = [
            ("➕ Add New User", self.add_new_user),
            ("🔐 Change Password", self.change_password),
            ("📧 Send Email", self.send_email),
            ("🔍 Search Users", self.search_users)
        ]
        
        for i, (text, command) in enumerate(quick_actions):
            action_btn = ttk.Button(actions_frame, text=text, command=command, 
                                  style="Secondary.TButton", width=20)
            action_btn.grid(row=i+1, column=0, pady=5, sticky="ew")
        
        # Professional footer
        footer_frame = ttk.Frame(card_frame, style="Professional.TFrame")
        footer_frame.grid(row=3, column=0, sticky="ew", pady=(20, 0))
        footer_frame.grid_columnconfigure(0, weight=1)
        
        logout_btn = ttk.Button(footer_frame, text="🚪 Logout", 
                               command=self.app.logout, 
                               style="Secondary.TButton", width=15)
        logout_btn.grid(row=0, column=0, pady=10)
        
        # Professional footer text
        footer_text = ttk.Label(footer_frame, 
                               text="© 2024 Enterprise CMS. Professional customer management system.", 
                               style="Caption.TLabel")
        footer_text.grid(row=1, column=0, pady=(5, 0))
    
    def _create_stat_card(self, parent, title, value, icon, column):
        """Create a professional stat card"""
        card_frame = ttk.Frame(parent, style="Professional.TFrame")
        card_frame.grid(row=0, column=column, sticky="ew", padx=5, pady=5)
        card_frame.grid_columnconfigure(0, weight=1)
        
        # Card content
        icon_label = ttk.Label(card_frame, text=icon, font=("Segoe UI", 24))
        icon_label.grid(row=0, column=0, pady=(10, 5))
        
        value_label = ttk.Label(card_frame, text=value, 
                               font=("Segoe UI", 18, "bold"), 
                               foreground=self.app.style_manager.colors['primary'])
        value_label.grid(row=1, column=0, pady=(0, 5))
        
        title_label = ttk.Label(card_frame, text=title, 
                               style="Caption.TLabel")
        title_label.grid(row=2, column=0, pady=(0, 10))
    
    def show_profile(self):
        """Show profile page"""
        self.show_profile_dialog()
    
    def show_settings(self):
        """Show settings page"""
        self.app.message_box.show_info("Settings", "Settings functionality will be implemented")
    
    def add_new_user(self):
        """Add new user"""
        self.app.show_register_page()
    
    def change_password(self):
        """Change password"""
        self.show_change_password_dialog()
    
    def send_email(self):
        """Send email"""
        self.app.message_box.show_info("Send Email", "Email functionality will be implemented")
    
    def search_users(self):
        """Search users"""
        self.app.show_users_list()
    
    def show_profile_dialog(self):
        """Show profile management dialog"""
        # Get current user data
        user_data = self.app.database_service.get_customer_by_email(self.user[3])
        if not user_data:
            self.app.message_box.show_error("Error", "User data not found!")
            return
        
        # Create professional profile dialog
        dialog = tk.Toplevel(self.app.root)
        dialog.title("My Profile - Enterprise CMS")
        dialog.geometry("500x600")
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
        y = (dialog.winfo_screenheight() // 2) - (600 // 2)
        dialog.geometry(f"500x600+{x}+{y}")
        
        # Create main container
        main_container = ttk.Frame(dialog, style="Professional.TFrame")
        main_container.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
        main_container.grid_columnconfigure(0, weight=1)
        
        # Professional header
        header_frame = ttk.Frame(main_container, style="Professional.TFrame")
        header_frame.grid(row=0, column=0, sticky="ew", pady=(20, 15))
        header_frame.grid_columnconfigure(0, weight=1)
        
        # Profile icon and title
        title_frame = ttk.Frame(header_frame, style="Professional.TFrame")
        title_frame.grid(row=0, column=0, pady=(0, 10))
        title_frame.grid_columnconfigure(1, weight=1)
        
        profile_icon = ttk.Label(title_frame, text="👤", font=("Segoe UI", 24))
        profile_icon.grid(row=0, column=0, padx=(0, 15))
        
        title_label = ttk.Label(title_frame, text="My Profile", 
                               style="Title.TLabel", font=("Segoe UI", 18, "bold"))
        title_label.grid(row=0, column=1, sticky="w")
        
        subtitle_label = ttk.Label(header_frame, text="Manage your account information", 
                                 style="Subtitle.TLabel", font=("Segoe UI", 11))
        subtitle_label.grid(row=1, column=0, pady=(0, 10))
        
        # Main content area
        content_frame = ttk.Frame(main_container, style="Professional.TFrame")
        content_frame.grid(row=1, column=0, sticky="nsew", padx=30, pady=(0, 20))
        content_frame.grid_columnconfigure(0, weight=1)
        
        # Profile form
        form_frame = ttk.Frame(content_frame, style="Professional.TFrame")
        form_frame.grid(row=0, column=0, sticky="ew", pady=(0, 20))
        form_frame.grid_columnconfigure(0, weight=1)
        
        # First Name
        first_name_frame = ttk.Frame(form_frame, style="Professional.TFrame")
        first_name_frame.grid(row=0, column=0, sticky="ew", pady=(0, 15))
        first_name_frame.grid_columnconfigure(0, weight=1)
        
        first_name_label = ttk.Label(first_name_frame, text="First Name", 
                                   style="Body.TLabel", font=("Segoe UI", 10, "bold"))
        first_name_label.grid(row=0, column=0, sticky="w", pady=(0, 5))
        
        first_name_entry = ttk.Entry(first_name_frame, style="Professional.TEntry", 
                                   font=("Segoe UI", 11), width=40)
        first_name_entry.grid(row=1, column=0, sticky="ew", pady=(0, 5))
        first_name_entry.insert(0, user_data[1])  # first_name
        
        # Last Name
        last_name_frame = ttk.Frame(form_frame, style="Professional.TFrame")
        last_name_frame.grid(row=1, column=0, sticky="ew", pady=(0, 15))
        last_name_frame.grid_columnconfigure(0, weight=1)
        
        last_name_label = ttk.Label(last_name_frame, text="Last Name", 
                                  style="Body.TLabel", font=("Segoe UI", 10, "bold"))
        last_name_label.grid(row=0, column=0, sticky="w", pady=(0, 5))
        
        last_name_entry = ttk.Entry(last_name_frame, style="Professional.TEntry", 
                                  font=("Segoe UI", 11), width=40)
        last_name_entry.grid(row=1, column=0, sticky="ew", pady=(0, 5))
        last_name_entry.insert(0, user_data[2])  # last_name
        
        # Email (read-only)
        email_frame = ttk.Frame(form_frame, style="Professional.TFrame")
        email_frame.grid(row=2, column=0, sticky="ew", pady=(0, 15))
        email_frame.grid_columnconfigure(0, weight=1)
        
        email_label = ttk.Label(email_frame, text="Email Address", 
                              style="Body.TLabel", font=("Segoe UI", 10, "bold"))
        email_label.grid(row=0, column=0, sticky="w", pady=(0, 5))
        
        email_entry = ttk.Entry(email_frame, style="Professional.TEntry", 
                              font=("Segoe UI", 11), width=40, state="readonly")
        email_entry.grid(row=1, column=0, sticky="ew", pady=(0, 5))
        email_entry.configure(state="normal")
        email_entry.insert(0, user_data[3])  # email
        email_entry.configure(state="readonly")
        
        # Phone
        phone_frame = ttk.Frame(form_frame, style="Professional.TFrame")
        phone_frame.grid(row=3, column=0, sticky="ew", pady=(0, 20))
        phone_frame.grid_columnconfigure(0, weight=1)
        
        phone_label = ttk.Label(phone_frame, text="Phone Number", 
                              style="Body.TLabel", font=("Segoe UI", 10, "bold"))
        phone_label.grid(row=0, column=0, sticky="w", pady=(0, 5))
        
        phone_entry = ttk.Entry(phone_frame, style="Professional.TEntry", 
                              font=("Segoe UI", 11), width=40)
        phone_entry.grid(row=1, column=0, sticky="ew", pady=(0, 5))
        phone_entry.insert(0, user_data[4])  # phone
        
        # Status label
        status_frame = ttk.Frame(content_frame, style="Professional.TFrame")
        status_frame.grid(row=1, column=0, sticky="ew", pady=(0, 20))
        status_frame.grid_columnconfigure(0, weight=1)
        
        status_label = ttk.Label(status_frame, text="", 
                               style="Caption.TLabel", font=("Segoe UI", 9), 
                               wraplength=400, justify="center")
        status_label.grid(row=0, column=0, pady=5)
        
        # Buttons section
        buttons_frame = ttk.Frame(content_frame, style="Professional.TFrame")
        buttons_frame.grid(row=2, column=0, sticky="ew", pady=(0, 15))
        buttons_frame.grid_columnconfigure(0, weight=1)
        buttons_frame.grid_columnconfigure(1, weight=1)
        
        def save_profile():
            """Save profile changes"""
            first_name = first_name_entry.get().strip()
            last_name = last_name_entry.get().strip()
            phone = phone_entry.get().strip()
            
            if not first_name or not last_name or not phone:
                status_label.config(text="❌ Please fill in all fields", 
                                  foreground=self.app.style_manager.colors['error'])
                return
            
            try:
                # Update profile in database
                success = self.app.database_service.update_customer_profile(
                    self.user[3], first_name, last_name, phone
                )
                
                if success:
                    status_label.config(text="✅ Profile updated successfully!", 
                                      foreground=self.app.style_manager.colors['success'])
                    # Update user data in memory
                    self.user = (self.user[0], first_name, last_name, self.user[3])
                    # Close dialog after a short delay
                    dialog.after(1500, dialog.destroy)
                else:
                    status_label.config(text="❌ Failed to update profile", 
                                      foreground=self.app.style_manager.colors['error'])
                    
            except Exception as e:
                status_label.config(text=f"❌ Error: {str(e)}", 
                                  foreground=self.app.style_manager.colors['error'])
        
        def cancel_profile():
            """Cancel profile changes"""
            dialog.destroy()
        
        # Save button
        save_btn = ttk.Button(buttons_frame, text="💾 Save Changes", 
                             command=save_profile, 
                             style="Primary.TButton", width=20)
        save_btn.grid(row=0, column=0, padx=(0, 10), pady=10)
        
        # Cancel button
        cancel_btn = ttk.Button(buttons_frame, text="❌ Cancel", 
                               command=cancel_profile, 
                               style="Secondary.TButton", width=20)
        cancel_btn.grid(row=0, column=1, padx=(10, 0), pady=10)
        
        # Focus on first name field
        first_name_entry.focus_set()
        
        # Bind Enter key to save
        dialog.bind('<Return>', lambda e: save_profile())
        dialog.bind('<Escape>', lambda e: cancel_profile())
        
        # Make dialog modal
        dialog.focus_set()
        dialog.wait_window()
    
    def show_change_password_dialog(self):
        """Show change password dialog"""
        # Create professional change password dialog
        dialog = tk.Toplevel(self.app.root)
        dialog.title("Change Password - Enterprise CMS")
        dialog.geometry("450x500")
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
        x = (dialog.winfo_screenwidth() // 2) - (450 // 2)
        y = (dialog.winfo_screenheight() // 2) - (500 // 2)
        dialog.geometry(f"450x500+{x}+{y}")
        
        # Create main container
        main_container = ttk.Frame(dialog, style="Professional.TFrame")
        main_container.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
        main_container.grid_columnconfigure(0, weight=1)
        
        # Professional header
        header_frame = ttk.Frame(main_container, style="Professional.TFrame")
        header_frame.grid(row=0, column=0, sticky="ew", pady=(20, 15))
        header_frame.grid_columnconfigure(0, weight=1)
        
        # Lock icon and title
        title_frame = ttk.Frame(header_frame, style="Professional.TFrame")
        title_frame.grid(row=0, column=0, pady=(0, 10))
        title_frame.grid_columnconfigure(1, weight=1)
        
        lock_icon = ttk.Label(title_frame, text="🔐", font=("Segoe UI", 24))
        lock_icon.grid(row=0, column=0, padx=(0, 15))
        
        title_label = ttk.Label(title_frame, text="Change Password", 
                               style="Title.TLabel", font=("Segoe UI", 18, "bold"))
        title_label.grid(row=0, column=1, sticky="w")
        
        subtitle_label = ttk.Label(header_frame, text="Update your account password", 
                                 style="Subtitle.TLabel", font=("Segoe UI", 11))
        subtitle_label.grid(row=1, column=0, pady=(0, 10))
        
        # Main content area
        content_frame = ttk.Frame(main_container, style="Professional.TFrame")
        content_frame.grid(row=1, column=0, sticky="nsew", padx=30, pady=(0, 20))
        content_frame.grid_columnconfigure(0, weight=1)
        
        # Password form
        form_frame = ttk.Frame(content_frame, style="Professional.TFrame")
        form_frame.grid(row=0, column=0, sticky="ew", pady=(0, 20))
        form_frame.grid_columnconfigure(0, weight=1)
        
        # Current Password
        current_password_frame = ttk.Frame(form_frame, style="Professional.TFrame")
        current_password_frame.grid(row=0, column=0, sticky="ew", pady=(0, 15))
        current_password_frame.grid_columnconfigure(0, weight=1)
        
        current_password_label = ttk.Label(current_password_frame, text="Current Password", 
                                         style="Body.TLabel", font=("Segoe UI", 10, "bold"))
        current_password_label.grid(row=0, column=0, sticky="w", pady=(0, 5))
        
        current_password_entry = ttk.Entry(current_password_frame, show="●", 
                                         style="Professional.TEntry", 
                                         font=("Segoe UI", 11), width=40)
        current_password_entry.grid(row=1, column=0, sticky="ew", pady=(0, 5))
        
        # New Password
        new_password_frame = ttk.Frame(form_frame, style="Professional.TFrame")
        new_password_frame.grid(row=1, column=0, sticky="ew", pady=(0, 15))
        new_password_frame.grid_columnconfigure(0, weight=1)
        
        new_password_label = ttk.Label(new_password_frame, text="New Password", 
                                     style="Body.TLabel", font=("Segoe UI", 10, "bold"))
        new_password_label.grid(row=0, column=0, sticky="w", pady=(0, 5))
        
        new_password_entry = ttk.Entry(new_password_frame, show="●", 
                                     style="Professional.TEntry", 
                                     font=("Segoe UI", 11), width=40)
        new_password_entry.grid(row=1, column=0, sticky="ew", pady=(0, 5))
        
        # Confirm New Password
        confirm_password_frame = ttk.Frame(form_frame, style="Professional.TFrame")
        confirm_password_frame.grid(row=2, column=0, sticky="ew", pady=(0, 20))
        confirm_password_frame.grid_columnconfigure(0, weight=1)
        
        confirm_password_label = ttk.Label(confirm_password_frame, text="Confirm New Password", 
                                         style="Body.TLabel", font=("Segoe UI", 10, "bold"))
        confirm_password_label.grid(row=0, column=0, sticky="w", pady=(0, 5))
        
        confirm_password_entry = ttk.Entry(confirm_password_frame, show="●", 
                                         style="Professional.TEntry", 
                                         font=("Segoe UI", 11), width=40)
        confirm_password_entry.grid(row=1, column=0, sticky="ew", pady=(0, 5))
        
        # Status label
        status_frame = ttk.Frame(content_frame, style="Professional.TFrame")
        status_frame.grid(row=1, column=0, sticky="ew", pady=(0, 20))
        status_frame.grid_columnconfigure(0, weight=1)
        
        status_label = ttk.Label(status_frame, text="", 
                               style="Caption.TLabel", font=("Segoe UI", 9), 
                               wraplength=400, justify="center")
        status_label.grid(row=0, column=0, pady=5)
        
        # Buttons section
        buttons_frame = ttk.Frame(content_frame, style="Professional.TFrame")
        buttons_frame.grid(row=2, column=0, sticky="ew", pady=(0, 15))
        buttons_frame.grid_columnconfigure(0, weight=1)
        buttons_frame.grid_columnconfigure(1, weight=1)
        
        def change_password():
            """Handle password change"""
            current_password = current_password_entry.get()
            new_password = new_password_entry.get()
            confirm_password = confirm_password_entry.get()
            
            if not current_password or not new_password or not confirm_password:
                status_label.config(text="❌ Please fill in all fields", 
                                  foreground=self.app.style_manager.colors['error'])
                return
            
            if new_password != confirm_password:
                status_label.config(text="❌ New passwords do not match", 
                                  foreground=self.app.style_manager.colors['error'])
                return
            
            if len(new_password) < 6:
                status_label.config(text="❌ New password must be at least 6 characters", 
                                  foreground=self.app.style_manager.colors['error'])
                return
            
            try:
                # Hash the passwords
                current_hash = hashlib.sha256(current_password.encode()).hexdigest()
                new_hash = hashlib.sha256(new_password.encode()).hexdigest()
                
                # Verify current password
                user = self.app.database_service.authenticate_customer(
                    self.user[3], current_hash
                )
                
                if not user:
                    status_label.config(text="❌ Current password is incorrect", 
                                      foreground=self.app.style_manager.colors['error'])
                    return
                
                # Update password in database
                success = self.app.database_service.update_customer_password(
                    self.user[3], new_hash
                )
                
                if success:
                    status_label.config(text="✅ Password changed successfully!", 
                                      foreground=self.app.style_manager.colors['success'])
                    # Clear saved credentials if they exist
                    self.app.auth_service.clear_saved_credentials()
                    # Close dialog after a short delay
                    dialog.after(1500, dialog.destroy)
                else:
                    status_label.config(text="❌ Failed to change password", 
                                      foreground=self.app.style_manager.colors['error'])
                    
            except Exception as e:
                status_label.config(text=f"❌ Error: {str(e)}", 
                                  foreground=self.app.style_manager.colors['error'])
        
        def cancel_change():
            """Cancel password change"""
            dialog.destroy()
        
        # Change button
        change_btn = ttk.Button(buttons_frame, text="🔐 Change Password", 
                               command=change_password, 
                               style="Primary.TButton", width=20)
        change_btn.grid(row=0, column=0, padx=(0, 10), pady=10)
        
        # Cancel button
        cancel_btn = ttk.Button(buttons_frame, text="❌ Cancel", 
                               command=cancel_change, 
                               style="Secondary.TButton", width=20)
        cancel_btn.grid(row=0, column=1, padx=(10, 0), pady=10)
        
        # Focus on current password field
        current_password_entry.focus_set()
        
        # Bind Enter key to change password
        dialog.bind('<Return>', lambda e: change_password())
        dialog.bind('<Escape>', lambda e: cancel_change())
        
        # Make dialog modal
        dialog.focus_set()
        dialog.wait_window()
