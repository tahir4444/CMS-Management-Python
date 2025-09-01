"""Users page component"""

import tkinter as tk
from tkinter import ttk


class UsersPage:
    """Users page for the application"""
    
    def __init__(self, app):
        self.app = app
        self.main_frame = app.main_frame
    
    def show(self):
        """Show the users page"""
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
        
        # Professional title
        title_label = ttk.Label(header_frame, text="👥 Users Management", 
                               style="Title.TLabel")
        title_label.grid(row=0, column=0, pady=(0, 10))
        
        # Professional subtitle
        subtitle = ttk.Label(header_frame, text="Manage your customer database", 
                           style="Subtitle.TLabel")
        subtitle.grid(row=1, column=0, pady=(0, 20))
        
        # Professional navigation section
        nav_frame = ttk.Frame(card_frame, style="Professional.TFrame")
        nav_frame.grid(row=1, column=0, sticky="ew", pady=(0, 30))
        nav_frame.grid_columnconfigure(0, weight=1)
        nav_frame.grid_columnconfigure(1, weight=1)
        nav_frame.grid_columnconfigure(2, weight=1)
        
        # Professional navigation buttons
        dashboard_btn = ttk.Button(nav_frame, text="🏠 Dashboard", 
                                  command=lambda: self.app.show_dashboard(self.app.current_user), 
                                  style="Primary.TButton", width=18)
        dashboard_btn.grid(row=0, column=0, padx=10, pady=10)
        
        add_user_btn = ttk.Button(nav_frame, text="➕ Add New User", 
                                 command=self.add_new_user, 
                                 style="Success.TButton", width=18)
        add_user_btn.grid(row=0, column=1, padx=10, pady=10)
        
        export_btn = ttk.Button(nav_frame, text="📤 Export Data", 
                               command=self.export_users, 
                               style="Secondary.TButton", width=18)
        export_btn.grid(row=0, column=2, padx=10, pady=10)
        
        # Professional search and filter section
        search_frame = ttk.Frame(card_frame, style="Professional.TFrame")
        search_frame.grid(row=2, column=0, sticky="ew", pady=(0, 20))
        search_frame.grid_columnconfigure(0, weight=1)
        search_frame.grid_columnconfigure(1, weight=1)
        search_frame.grid_columnconfigure(2, weight=1)
        
        # Professional search field
        search_label = ttk.Label(search_frame, text="Search Users:", 
                                style="Body.TLabel")
        search_label.grid(row=0, column=0, sticky="w", pady=(0, 8))
        
        self.search_entry = ttk.Entry(search_frame, style="Professional.TEntry", 
                                     font=("Segoe UI", 11), width=30)
        self.search_entry.grid(row=1, column=0, sticky="ew", pady=(0, 5))
        self.search_entry.bind('<KeyRelease>', self.filter_users)
        
        # Professional filter dropdown
        filter_label = ttk.Label(search_frame, text="Filter by Status:", 
                                style="Body.TLabel")
        filter_label.grid(row=0, column=1, sticky="w", pady=(0, 8), padx=(20, 0))
        
        self.filter_var = tk.StringVar(value="All")
        filter_combo = ttk.Combobox(search_frame, textvariable=self.filter_var, 
                                   values=["All", "Active", "Inactive", "New"], 
                                   state="readonly", width=15)
        filter_combo.grid(row=1, column=1, sticky="ew", pady=(0, 5), padx=(20, 0))
        filter_combo.bind('<<ComboboxSelected>>', self.filter_users)
        
        # Professional refresh button
        refresh_btn = ttk.Button(search_frame, text="🔄 Refresh", 
                                command=self.refresh_users, 
                                style="Secondary.TButton", width=12)
        refresh_btn.grid(row=1, column=2, sticky="e", pady=(0, 5))
        
        # Professional users table
        table_frame = ttk.Frame(card_frame, style="Professional.TFrame")
        table_frame.grid(row=3, column=0, sticky="ew", pady=(0, 30))
        table_frame.grid_columnconfigure(0, weight=1)
        
        # Professional table title
        table_title = ttk.Label(table_frame, text="Customer Database", 
                               style="Heading.TLabel")
        table_title.grid(row=0, column=0, pady=(0, 15), sticky="w")
        
        # Professional treeview for users
        columns = ('ID', 'Name', 'Email', 'Phone', 'Status', 'Created', 'Actions')
        self.tree = ttk.Treeview(table_frame, columns=columns, show='headings', height=10)
        
        # Bind double-click event for editing
        self.tree.bind('<Double-1>', self.on_user_double_click)
        
        # Professional column headers
        self.tree.heading('ID', text='ID')
        self.tree.heading('Name', text='Full Name')
        self.tree.heading('Email', text='Email Address')
        self.tree.heading('Phone', text='Phone Number')
        self.tree.heading('Status', text='Status')
        self.tree.heading('Created', text='Created Date')
        self.tree.heading('Actions', text='Actions')
        
        # Professional column widths
        self.tree.column('ID', width=50, anchor='center')
        self.tree.column('Name', width=150, anchor='w')
        self.tree.column('Email', width=200, anchor='w')
        self.tree.column('Phone', width=120, anchor='w')
        self.tree.column('Status', width=80, anchor='center')
        self.tree.column('Created', width=100, anchor='center')
        self.tree.column('Actions', width=120, anchor='center')
        
        # Professional scrollbar
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Professional grid layout for tree and scrollbar
        self.tree.grid(row=1, column=0, sticky="nsew", pady=(0, 10))
        scrollbar.grid(row=1, column=1, sticky="ns")
        
        # Professional real data from database
        self.load_users_from_database()
        
        # Professional footer
        footer_frame = ttk.Frame(card_frame, style="Professional.TFrame")
        footer_frame.grid(row=4, column=0, sticky="ew", pady=(20, 0))
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
    
    def load_users_from_database(self):
        """Load real users data from database"""
        try:
            # Get all users from database
            users = self.app.database_service.get_all_customers()
            
            # Clear existing items
            for item in self.tree.get_children():
                self.tree.delete(item)
            
            # Add users to treeview
            for user in users:
                user_id, first_name, last_name, email, phone, created_at = user
                
                # Format the date
                try:
                    from datetime import datetime
                    date_obj = datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S')
                    formatted_date = date_obj.strftime('%Y-%m-%d')
                except:
                    formatted_date = created_at
                
                # Determine status based on creation date
                try:
                    from datetime import datetime, timedelta
                    created_date = datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S')
                    days_old = (datetime.now() - created_date).days
                    
                    if days_old == 0:
                        status = "New"
                    elif days_old <= 7:
                        status = "Active"
                    else:
                        status = "Active"
                except:
                    status = "Active"
                
                # Insert into treeview
                self.tree.insert('', 'end', values=(
                    user_id,
                    f"{first_name} {last_name}",
                    email,
                    phone,
                    status,
                    formatted_date,
                    "Edit | Delete"
                ))
                
        except Exception as e:
            print(f"Error loading users: {e}")
            # Fallback to empty list
            pass
    
    def filter_users(self, event=None):
        """Filter users based on search and filter criteria"""
        try:
            search_term = self.search_entry.get().strip().lower()
            status_filter = self.filter_var.get()
            
            # Clear existing items
            for item in self.tree.get_children():
                self.tree.delete(item)
            
            # Get all users
            users = self.app.database_service.get_all_customers()
            
            # Filter users
            for user in users:
                user_id, first_name, last_name, email, phone, created_at = user
                
                # Format the date
                try:
                    from datetime import datetime
                    date_obj = datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S')
                    formatted_date = date_obj.strftime('%Y-%m-%d')
                except:
                    formatted_date = created_at
                
                # Determine status based on creation date
                try:
                    from datetime import datetime, timedelta
                    created_date = datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S')
                    days_old = (datetime.now() - created_date).days
                    
                    if days_old == 0:
                        status = "New"
                    elif days_old <= 7:
                        status = "Active"
                    else:
                        status = "Active"
                except:
                    status = "Active"
                
                # Apply search filter
                if search_term:
                    search_text = f"{first_name} {last_name} {email}".lower()
                    if search_term not in search_text:
                        continue
                
                # Apply status filter
                if status_filter != "All" and status != status_filter:
                    continue
                
                # Insert into treeview
                self.tree.insert('', 'end', values=(
                    user_id,
                    f"{first_name} {last_name}",
                    email,
                    phone,
                    status,
                    formatted_date,
                    "Edit | Delete"
                ))
                
        except Exception as e:
            print(f"Error filtering users: {e}")
    
    def refresh_users(self):
        """Refresh the users list"""
        try:
            # Clear search and filter
            self.search_entry.delete(0, tk.END)
            self.filter_var.set("All")
            
            # Reload users
            self.load_users_from_database()
            
            # Show success message
            self.app.message_box.show_info("Refresh", "Users list refreshed successfully!")
            
        except Exception as e:
            self.app.message_box.show_error("Error", f"Failed to refresh users: {str(e)}")
    
    def add_new_user(self):
        """Add a new user"""
        self.app.show_register_page()
    
    def on_user_double_click(self, event):
        """Handle double-click on user row"""
        try:
            # Get selected item
            selection = self.tree.selection()
            if not selection:
                return
            
            # Get user data
            item = self.tree.item(selection[0])
            values = item['values']
            
            if values:
                user_id = values[0]
                self.edit_user(user_id)
                
        except Exception as e:
            self.app.message_box.show_error("Error", f"Failed to edit user: {str(e)}")
    
    def edit_user(self, user_id):
        """Edit user information"""
        try:
            # Get user data from database
            user = self.app.database_service.get_customer_by_id(user_id)
            if not user:
                self.app.message_box.show_error("Error", "User not found")
                return
            
            # Create edit dialog
            self.show_edit_user_dialog(user)
            
        except Exception as e:
            self.app.message_box.show_error("Error", f"Failed to get user data: {str(e)}")
    
    def show_edit_user_dialog(self, user):
        """Show dialog to edit user information"""
        # Create dialog
        dialog = tk.Toplevel(self.app.root)
        dialog.title("Edit User")
        dialog.geometry("500x400")
        dialog.resizable(False, False)
        dialog.transient(self.app.root)
        dialog.grab_set()
        
        # Center dialog
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - (500 // 2)
        y = (dialog.winfo_screenheight() // 2) - (400 // 2)
        dialog.geometry(f"500x400+{x}+{y}")
        
        # Create main frame
        main_frame = ttk.Frame(dialog, style="Professional.TFrame")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Title
        title_label = ttk.Label(main_frame, text="✏️ Edit User Information", 
                               style="Title.TLabel")
        title_label.pack(pady=(0, 20))
        
        # Form frame
        form_frame = ttk.Frame(main_frame, style="Professional.TFrame")
        form_frame.pack(fill="both", expand=True)
        
        # User ID (read-only)
        ttk.Label(form_frame, text="User ID:", style="Body.TLabel").pack(anchor="w", pady=(0, 5))
        id_entry = ttk.Entry(form_frame, style="Professional.TEntry", state="readonly")
        id_entry.pack(fill="x", pady=(0, 15))
        id_entry.insert(0, str(user[0]))
        
        # First Name
        ttk.Label(form_frame, text="First Name:", style="Body.TLabel").pack(anchor="w", pady=(0, 5))
        first_name_entry = ttk.Entry(form_frame, style="Professional.TEntry")
        first_name_entry.pack(fill="x", pady=(0, 15))
        first_name_entry.insert(0, user[1])
        
        # Last Name
        ttk.Label(form_frame, text="Last Name:", style="Body.TLabel").pack(anchor="w", pady=(0, 5))
        last_name_entry = ttk.Entry(form_frame, style="Professional.TEntry")
        last_name_entry.pack(fill="x", pady=(0, 15))
        last_name_entry.insert(0, user[2])
        
        # Email
        ttk.Label(form_frame, text="Email:", style="Body.TLabel").pack(anchor="w", pady=(0, 5))
        email_entry = ttk.Entry(form_frame, style="Professional.TEntry")
        email_entry.pack(fill="x", pady=(0, 15))
        email_entry.insert(0, user[3])
        
        # Phone
        ttk.Label(form_frame, text="Phone:", style="Body.TLabel").pack(anchor="w", pady=(0, 5))
        phone_entry = ttk.Entry(form_frame, style="Professional.TEntry")
        phone_entry.pack(fill="x", pady=(0, 20))
        phone_entry.insert(0, user[4])
        
        # Buttons frame
        buttons_frame = ttk.Frame(main_frame, style="Professional.TFrame")
        buttons_frame.pack(fill="x", pady=(20, 0))
        
        def save_changes():
            try:
                # Validate inputs
                first_name = first_name_entry.get().strip()
                last_name = last_name_entry.get().strip()
                email = email_entry.get().strip()
                phone = phone_entry.get().strip()
                
                if not all([first_name, last_name, email, phone]):
                    self.app.message_box.show_error("Error", "All fields are required")
                    return
                
                # Update user in database
                success = self.app.database_service.update_customer_profile(
                    user[3],  # original email
                    first_name,
                    last_name,
                    phone
                )
                
                if success:
                    self.app.message_box.show_info("Success", "User updated successfully!")
                    dialog.destroy()
                    self.refresh_users()
                else:
                    self.app.message_box.show_error("Error", "Failed to update user")
                    
            except Exception as e:
                self.app.message_box.show_error("Error", f"Failed to update user: {str(e)}")
        
        def delete_user():
            try:
                # Confirm deletion
                result = self.app.message_box.show_confirm(
                    "Confirm Delete",
                    f"Are you sure you want to delete user {user[1]} {user[2]}?\n\nThis action cannot be undone."
                )
                
                if result:
                    # Delete user from database
                    success = self.app.database_service.delete_customer(user[0])
                    
                    if success:
                        self.app.message_box.show_info("Success", "User deleted successfully!")
                        dialog.destroy()
                        self.refresh_users()
                    else:
                        self.app.message_box.show_error("Error", "Failed to delete user")
                        
            except Exception as e:
                self.app.message_box.show_error("Error", f"Failed to delete user: {str(e)}")
        
        # Save button
        save_btn = ttk.Button(buttons_frame, text="💾 Save Changes", 
                             command=save_changes, style="Success.TButton")
        save_btn.pack(side="left", padx=(0, 10))
        
        # Delete button
        delete_btn = ttk.Button(buttons_frame, text="🗑️ Delete User", 
                               command=delete_user, style="Secondary.TButton")
        delete_btn.pack(side="left", padx=(0, 10))
        
        # Cancel button
        cancel_btn = ttk.Button(buttons_frame, text="❌ Cancel", 
                               command=dialog.destroy, style="Secondary.TButton")
        cancel_btn.pack(side="right")
        
        # Focus on first name field
        first_name_entry.focus_set()
    
    def export_users(self):
        """Export users data"""
        try:
            import csv
            from datetime import datetime
            
            # Get filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"users_export_{timestamp}.csv"
            
            # Get all users
            users = self.app.database_service.get_all_customers()
            
            # Write to CSV
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                
                # Write header
                writer.writerow(['ID', 'First Name', 'Last Name', 'Email', 'Phone', 'Created Date'])
                
                # Write user data
                for user in users:
                    writer.writerow([
                        user[0],  # ID
                        user[1],  # First Name
                        user[2],  # Last Name
                        user[3],  # Email
                        user[4],  # Phone
                        user[5]   # Created Date
                    ])
            
            self.app.message_box.show_info("Export Success", f"Users exported to {filename}")
            
        except Exception as e:
            self.app.message_box.show_error("Export Error", f"Failed to export users: {str(e)}")
