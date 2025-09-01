#!/usr/bin/env python3
"""
Database Viewer Script
Simple script to view the customers database
"""

import sqlite3
import sys
from datetime import datetime

def view_database():
    """View the customers database"""
    try:
        # Connect to database
        conn = sqlite3.connect('customers.db')
        cursor = conn.cursor()
        
        print("=" * 60)
        print("CUSTOMER MANAGEMENT SYSTEM - DATABASE VIEWER")
        print("=" * 60)
        
        # Get table structure
        print("\n📋 TABLE STRUCTURE:")
        print("-" * 40)
        cursor.execute("PRAGMA table_info(customers)")
        columns = cursor.fetchall()
        
        for col in columns:
            print(f"Column: {col[1]} ({col[2]}) - {'NOT NULL' if col[3] else 'NULL'} - {'PRIMARY KEY' if col[5] else ''}")
        
        # Get total records
        cursor.execute("SELECT COUNT(*) FROM customers")
        total_records = cursor.fetchone()[0]
        print(f"\n📊 TOTAL RECORDS: {total_records}")
        
        if total_records > 0:
            # Get all customers
            print("\n👥 ALL CUSTOMERS:")
            print("-" * 80)
            print(f"{'ID':<5} {'First Name':<15} {'Last Name':<15} {'Email':<25} {'Phone':<15} {'Created'}")
            print("-" * 80)
            
            cursor.execute('''
                SELECT id, first_name, last_name, email, phone, created_at 
                FROM customers 
                ORDER BY created_at DESC
            ''')
            
            customers = cursor.fetchall()
            for customer in customers:
                created_date = customer[5][:10] if customer[5] else "N/A"
                print(f"{customer[0]:<5} {customer[1]:<15} {customer[2]:<15} {customer[3]:<25} {customer[4]:<15} {created_date}")
            
            # Show some statistics
            print("\n📈 STATISTICS:")
            print("-" * 40)
            
            # Recent registrations (last 7 days)
            cursor.execute('''
                SELECT COUNT(*) FROM customers 
                WHERE created_at >= date('now', '-7 days')
            ''')
            recent = cursor.fetchone()[0]
            print(f"Registrations in last 7 days: {recent}")
            
            # Most common email domains
            cursor.execute('''
                SELECT 
                    SUBSTR(email, INSTR(email, '@') + 1) as domain,
                    COUNT(*) as count
                FROM customers 
                GROUP BY domain 
                ORDER BY count DESC 
                LIMIT 5
            ''')
            domains = cursor.fetchall()
            if domains:
                print("\nMost common email domains:")
                for domain, count in domains:
                    print(f"  {domain}: {count} users")
        
        else:
            print("\n❌ No customers found in database.")
            print("Register some customers through the application first!")
        
        conn.close()
        
    except FileNotFoundError:
        print("❌ Database file 'customers.db' not found!")
        print("Run the main application first to create the database.")
    except Exception as e:
        print(f"❌ Error viewing database: {str(e)}")

def export_to_csv():
    """Export database to CSV file"""
    try:
        import csv
        
        conn = sqlite3.connect('customers.db')
        cursor = conn.cursor()
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"database_export_{timestamp}.csv"
        
        # Fetch all customers
        cursor.execute('''
            SELECT id, first_name, last_name, email, phone, created_at 
            FROM customers 
            ORDER BY created_at DESC
        ''')
        customers = cursor.fetchall()
        
        # Write to CSV file
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['ID', 'First Name', 'Last Name', 'Email', 'Phone', 'Created At'])
            
            for customer in customers:
                writer.writerow(customer)
        
        print(f"\n✅ Database exported to: {filename}")
        conn.close()
        
    except Exception as e:
        print(f"❌ Error exporting database: {str(e)}")

if __name__ == "__main__":
    print("Database Viewer for Customer Management System")
    print("=" * 50)
    
    while True:
        print("\nOptions:")
        print("1. View Database")
        print("2. Export to CSV")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            view_database()
        elif choice == "2":
            export_to_csv()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
