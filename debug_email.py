#!/usr/bin/env python3
"""
Email Debugging Script for Enterprise CMS
Helps diagnose email delivery issues with detailed logging.
"""

import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import sys

def load_smtp_config():
    """Load SMTP configuration from smtp_config.py"""
    try:
        from smtp_config import SMTP_CONFIG
        return SMTP_CONFIG
    except ImportError:
        print("❌ Error: smtp_config.py not found!")
        return None

def debug_email_send(smtp_config, recipient_email):
    """Send a test email with detailed debugging information"""
    try:
        print("🔍 EMAIL DEBUGGING STARTED")
        print("=" * 50)
        
        # Get sender email
        sender_email = smtp_config.get('sender_email', smtp_config['username'])
        
        print(f"📧 Configuration:")
        print(f"   SMTP Server: {smtp_config['server']}")
        print(f"   Port: {smtp_config['port']}")
        print(f"   Username: {smtp_config['username']}")
        print(f"   Sender Email: {sender_email}")
        print(f"   Recipient: {recipient_email}")
        print()
        
        # Create message
        msg = MIMEMultipart()
        sender_name = smtp_config.get('sender_name', 'Enterprise CMS')
        msg['From'] = f"{sender_name} <{sender_email}>"
        msg['To'] = recipient_email
        msg['Subject'] = "🔍 Email Debug Test - Enterprise CMS"
        
        # Simple text email for testing
        body = f"""
        Email Debug Test
        
        This is a test email to verify email delivery.
        
        Test Details:
        - Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        - Sender: {sender_email}
        - Recipient: {recipient_email}
        - SMTP Server: {smtp_config['server']}
        
        If you receive this email, the SMTP service is working correctly.
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        print("🔗 Step 1: Connecting to SMTP server...")
        server = smtplib.SMTP(smtp_config['server'], smtp_config['port'])
        print("✅ SMTP connection established")
        
        print("🔒 Step 2: Starting TLS encryption...")
        server.starttls(context=ssl.create_default_context())
        print("✅ TLS encryption started")
        
        print("🔐 Step 3: Authenticating...")
        server.login(smtp_config['username'], smtp_config['password'])
        print("✅ Authentication successful")
        
        print("📤 Step 4: Sending email...")
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        print("✅ Email sent successfully")
        
        print("🔌 Step 5: Closing connection...")
        server.quit()
        print("✅ Connection closed")
        
        print()
        print("🎉 EMAIL DEBUG COMPLETED SUCCESSFULLY!")
        print("✅ All steps completed without errors")
        print()
        print("📋 Troubleshooting Tips:")
        print("   1. Check your Gmail inbox (including spam folder)")
        print("   2. Wait 1-2 minutes for email delivery")
        print("   3. Check Gmail filters and settings")
        print("   4. Verify the email address is correct")
        
        return True
        
    except smtplib.SMTPAuthenticationError as e:
        print(f"❌ Authentication Error: {e}")
        print("   Check your Brevo username and password")
        return False
        
    except smtplib.SMTPConnectError as e:
        print(f"❌ Connection Error: {e}")
        print("   Check your internet connection and SMTP settings")
        return False
        
    except smtplib.SMTPRecipientsRefused as e:
        print(f"❌ Recipient Error: {e}")
        print("   Check the recipient email address")
        return False
        
    except smtplib.SMTPSenderRefused as e:
        print(f"❌ Sender Error: {e}")
        print("   The sender email address is not authorized")
        print("   You may need to verify your domain in Brevo")
        return False
        
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")
        return False

def main():
    """Main debugging function"""
    print("🔍 ENTERPRISE CMS - EMAIL DEBUGGING")
    print("=" * 50)
    
    # Load SMTP configuration
    smtp_config = load_smtp_config()
    if not smtp_config:
        return False
    
    # Get recipient email
    if len(sys.argv) > 1:
        recipient_email = sys.argv[1]
    else:
        recipient_email = input("📧 Enter recipient email address: ").strip()
    
    if not recipient_email:
        print("❌ No recipient email provided.")
        return False
    
    print()
    
    # Run debug test
    success = debug_email_send(smtp_config, recipient_email)
    
    if not success:
        print()
        print("❌ EMAIL DEBUG FAILED!")
        print("Please check the error messages above.")
    
    return success

if __name__ == "__main__":
    main()
