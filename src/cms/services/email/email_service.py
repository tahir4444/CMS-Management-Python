"""Email service for sending emails"""

import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from ...config.smtp_config import DEFAULT_SMTP_CONFIG


class EmailService:
    """Service for handling email operations"""
    
    def __init__(self, smtp_config=None):
        self.smtp_config = smtp_config or DEFAULT_SMTP_CONFIG
    
    def send_password_reset_email(self, user_email: str, temp_password: str, user_name: str) -> bool:
        """Send password reset email"""
        try:
            msg = MIMEMultipart('alternative')
            sender_email = self.smtp_config.get('sender_email', self.smtp_config['username'])
            sender_name = self.smtp_config.get('sender_name', 'Enterprise CMS')
            msg['From'] = f"{sender_name} <{sender_email}>"
            msg['To'] = user_email
            msg['Subject'] = "🔐 Password Reset - Enterprise CMS"
            
            # Plain text version
            text_body = f"""
Hello {user_name},

Your temporary password is: {temp_password}

Please use this password to log in and change it immediately.

Best regards,
Enterprise CMS Team
            """
            
            # HTML version with professional design
            html_body = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Password Reset - Enterprise CMS</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            margin: 0;
            padding: 0;
            background-color: #f8f9fa;
        }}
        .container {{
            max-width: 600px;
            margin: 0 auto;
            background-color: #ffffff;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            overflow: hidden;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px 40px;
            text-align: center;
        }}
        .header h1 {{
            margin: 0;
            font-size: 24px;
            font-weight: 600;
        }}
        .header p {{
            margin: 10px 0 0 0;
            opacity: 0.9;
            font-size: 14px;
        }}
        .content {{
            padding: 40px;
        }}
        .greeting {{
            font-size: 18px;
            color: #2c3e50;
            margin-bottom: 25px;
        }}
        .password-box {{
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            border: 2px solid #dee2e6;
            border-radius: 8px;
            padding: 20px;
            margin: 25px 0;
            text-align: center;
        }}
        .password-label {{
            font-size: 14px;
            color: #6c757d;
            margin-bottom: 10px;
            font-weight: 500;
        }}
        .password {{
            font-size: 24px;
            font-weight: bold;
            color: #495057;
            font-family: 'Courier New', monospace;
            letter-spacing: 2px;
            background: white;
            padding: 10px 20px;
            border-radius: 6px;
            border: 1px solid #ced4da;
            display: inline-block;
            margin: 5px 0;
        }}
        .instructions {{
            background-color: #e3f2fd;
            border-left: 4px solid #2196f3;
            padding: 20px;
            margin: 25px 0;
            border-radius: 0 6px 6px 0;
        }}
        .instructions h3 {{
            margin: 0 0 15px 0;
            color: #1976d2;
            font-size: 16px;
        }}
        .instructions ol {{
            margin: 0;
            padding-left: 20px;
        }}
        .instructions li {{
            margin-bottom: 8px;
            color: #424242;
        }}
        .security-note {{
            background-color: #fff3e0;
            border: 1px solid #ffb74d;
            border-radius: 6px;
            padding: 15px;
            margin: 25px 0;
        }}
        .security-note p {{
            margin: 0;
            color: #e65100;
            font-size: 14px;
            font-weight: 500;
        }}
        .footer {{
            background-color: #f8f9fa;
            padding: 25px 40px;
            text-align: center;
            border-top: 1px solid #dee2e6;
        }}
        .footer p {{
            margin: 5px 0;
            color: #6c757d;
            font-size: 13px;
        }}
        .logo {{
            font-size: 20px;
            margin-bottom: 10px;
        }}
        .button {{
            display: inline-block;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 12px 30px;
            text-decoration: none;
            border-radius: 6px;
            font-weight: 500;
            margin: 20px 0;
        }}
        @media only screen and (max-width: 600px) {{
            .container {{
                margin: 10px;
                border-radius: 6px;
            }}
            .header, .content, .footer {{
                padding: 20px;
            }}
            .password {{
                font-size: 20px;
                padding: 8px 15px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="logo">🔐</div>
            <h1>Password Reset</h1>
            <p>Enterprise CMS - Secure Account Recovery</p>
        </div>
        
        <div class="content">
            <div class="greeting">
                Hello <strong>{user_name}</strong>,
            </div>
            
            <p>We received a request to reset your password for your Enterprise CMS account. Your temporary password has been generated and is ready for use.</p>
            
            <div class="password-box">
                <div class="password-label">Your Temporary Password:</div>
                <div class="password">{temp_password}</div>
            </div>
            
            <div class="instructions">
                <h3>📋 Next Steps:</h3>
                <ol>
                    <li>Use the temporary password above to log into your account</li>
                    <li>Navigate to your account settings immediately after login</li>
                    <li>Change your password to a new secure password</li>
                    <li>Ensure your new password is strong and unique</li>
                </ol>
            </div>
            
            <div class="security-note">
                <p>⚠️ <strong>Security Notice:</strong> This temporary password will expire in 24 hours. For your security, please change it immediately after logging in.</p>
            </div>
            
            <p>If you didn't request this password reset, please contact our support team immediately.</p>
        </div>
        
        <div class="footer">
            <p><strong>Enterprise CMS</strong></p>
            <p>Professional Customer Management System</p>
            <p>🔒 Your security is our priority</p>
            <p style="font-size: 11px; margin-top: 15px;">
                This is an automated message. Please do not reply to this email.<br>
                If you need assistance, contact our support team.
            </p>
        </div>
    </div>
</body>
</html>
            """
            
            # Attach both plain text and HTML versions
            msg.attach(MIMEText(text_body, 'plain'))
            msg.attach(MIMEText(html_body, 'html'))
            
            if self.smtp_config['use_tls']:
                server = smtplib.SMTP(self.smtp_config['server'], self.smtp_config['port'])
                server.starttls(context=ssl.create_default_context())
            else:
                server = smtplib.SMTP_SSL(self.smtp_config['server'], self.smtp_config['port'])
            
            server.login(self.smtp_config['username'], self.smtp_config['password'])
            text = msg.as_string()
            server.sendmail(self.smtp_config['username'], user_email, text)
            server.quit()
            
            return True
            
        except Exception as e:
            print(f"Error sending email: {e}")
            return False
    
    def send_welcome_email(self, user_email: str, user_name: str, user_id: int) -> bool:
        """Send welcome email to new user"""
        try:
            msg = MIMEMultipart('alternative')
            sender_email = self.smtp_config.get('sender_email', self.smtp_config['username'])
            sender_name = self.smtp_config.get('sender_name', 'Enterprise CMS')
            msg['From'] = f"{sender_name} <{sender_email}>"
            msg['To'] = user_email
            msg['Subject'] = "🎉 Welcome to Enterprise CMS - Your Account is Ready!"
            
            # Plain text version
            text_body = f"""
Welcome to Enterprise CMS!

Dear {user_name},

Thank you for registering with Enterprise CMS! Your account has been successfully created and is ready to use.

Your Account Details:
- User ID: {user_id}
- Email: {user_email}
- Registration Date: {self._get_current_date()}

You can now log in to your account and start managing your customer database with our professional tools.

Best regards,
The Enterprise CMS Team
            """
            
            # HTML version with beautiful design
            html_body = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to Enterprise CMS</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }}
        .container {{
            max-width: 600px;
            margin: 20px auto;
            background-color: #ffffff;
            border-radius: 12px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            overflow: hidden;
        }}
        .header {{
            background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
            color: white;
            padding: 40px 40px 30px 40px;
            text-align: center;
            position: relative;
        }}
        .header::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grain" width="100" height="100" patternUnits="userSpaceOnUse"><circle cx="25" cy="25" r="1" fill="white" opacity="0.1"/><circle cx="75" cy="75" r="1" fill="white" opacity="0.1"/><circle cx="50" cy="10" r="0.5" fill="white" opacity="0.1"/><circle cx="10" cy="60" r="0.5" fill="white" opacity="0.1"/><circle cx="90" cy="40" r="0.5" fill="white" opacity="0.1"/></pattern></defs><rect width="100" height="100" fill="url(%23grain)"/></svg>');
        }}
        .header h1 {{
            margin: 0;
            font-size: 28px;
            font-weight: 700;
            position: relative;
            z-index: 1;
        }}
        .header p {{
            margin: 10px 0 0 0;
            opacity: 0.95;
            font-size: 16px;
            position: relative;
            z-index: 1;
        }}
        .welcome-icon {{
            font-size: 48px;
            margin-bottom: 15px;
            position: relative;
            z-index: 1;
        }}
        .content {{
            padding: 40px;
        }}
        .greeting {{
            font-size: 20px;
            color: #2c3e50;
            margin-bottom: 25px;
            font-weight: 600;
        }}
        .account-details {{
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            border: 2px solid #dee2e6;
            border-radius: 10px;
            padding: 25px;
            margin: 25px 0;
        }}
        .account-details h3 {{
            margin: 0 0 20px 0;
            color: #495057;
            font-size: 18px;
            text-align: center;
        }}
        .detail-row {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 12px 0;
            border-bottom: 1px solid #e9ecef;
        }}
        .detail-row:last-child {{
            border-bottom: none;
        }}
        .detail-label {{
            font-weight: 600;
            color: #6c757d;
            font-size: 14px;
        }}
        .detail-value {{
            font-weight: 500;
            color: #495057;
            font-size: 14px;
        }}
        .features {{
            background-color: #e8f5e8;
            border-left: 4px solid #4CAF50;
            padding: 25px;
            margin: 25px 0;
            border-radius: 0 8px 8px 0;
        }}
        .features h3 {{
            margin: 0 0 15px 0;
            color: #2e7d32;
            font-size: 18px;
        }}
        .features ul {{
            margin: 0;
            padding-left: 20px;
        }}
        .features li {{
            margin-bottom: 10px;
            color: #424242;
        }}
        .cta-section {{
            text-align: center;
            margin: 30px 0;
        }}
        .cta-button {{
            display: inline-block;
            background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
            color: white;
            padding: 15px 35px;
            text-decoration: none;
            border-radius: 8px;
            font-weight: 600;
            font-size: 16px;
            box-shadow: 0 4px 15px rgba(76, 175, 80, 0.3);
            transition: all 0.3s ease;
        }}
        .cta-button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(76, 175, 80, 0.4);
        }}
        .footer {{
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            padding: 30px 40px;
            text-align: center;
            border-top: 1px solid #dee2e6;
        }}
        .footer p {{
            margin: 5px 0;
            color: #6c757d;
            font-size: 14px;
        }}
        .social-links {{
            margin: 20px 0;
        }}
        .social-links a {{
            display: inline-block;
            margin: 0 10px;
            color: #6c757d;
            text-decoration: none;
            font-size: 16px;
        }}
        .highlight {{
            background: linear-gradient(120deg, #a8edea 0%, #fed6e3 100%);
            padding: 2px 6px;
            border-radius: 4px;
            font-weight: 600;
        }}
        @media only screen and (max-width: 600px) {{
            .container {{
                margin: 10px;
                border-radius: 8px;
            }}
            .header, .content, .footer {{
                padding: 20px;
            }}
            .detail-row {{
                flex-direction: column;
                align-items: flex-start;
                gap: 5px;
            }}
            .welcome-icon {{
                font-size: 36px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="welcome-icon">🎉</div>
            <h1>Welcome to Enterprise CMS!</h1>
            <p>Your Professional Customer Management Journey Begins</p>
        </div>
        
        <div class="content">
            <div class="greeting">
                Hello <span class="highlight">{user_name}</span>! 👋
            </div>
            
            <p>We're thrilled to welcome you to <strong>Enterprise CMS</strong>! Your account has been successfully created and is ready to help you manage your customer database with professional efficiency.</p>
            
            <div class="account-details">
                <h3>📋 Your Account Information</h3>
                <div class="detail-row">
                    <span class="detail-label">User ID:</span>
                    <span class="detail-value">#{user_id}</span>
                </div>
                <div class="detail-row">
                    <span class="detail-label">Email Address:</span>
                    <span class="detail-value">{user_email}</span>
                </div>
                <div class="detail-row">
                    <span class="detail-label">Registration Date:</span>
                    <span class="detail-value">{self._get_current_date()}</span>
                </div>
                <div class="detail-row">
                    <span class="detail-label">Account Status:</span>
                    <span class="detail-value">✅ Active</span>
                </div>
            </div>
            
            <div class="features">
                <h3>🚀 What You Can Do Now:</h3>
                <ul>
                    <li><strong>Dashboard Overview:</strong> Get insights into your customer database</li>
                    <li><strong>User Management:</strong> Add, edit, and manage customer records</li>
                    <li><strong>Search & Filter:</strong> Find customers quickly with advanced search</li>
                    <li><strong>Data Export:</strong> Export customer data in various formats</li>
                    <li><strong>Professional UI:</strong> Enjoy a modern, responsive interface</li>
                </ul>
            </div>
            
            <div class="cta-section">
                <p>Ready to get started? Log in to your account and explore the powerful features!</p>
                <a href="#" class="cta-button">🚀 Launch Enterprise CMS</a>
            </div>
            
            <p style="text-align: center; color: #6c757d; font-size: 14px; margin-top: 30px;">
                Need help? Our support team is here to assist you every step of the way.
            </p>
        </div>
        
        <div class="footer">
            <p><strong>Enterprise CMS</strong></p>
            <p>Professional Customer Management System</p>
            <div class="social-links">
                <a href="#">📧 Support</a>
                <a href="#">📖 Documentation</a>
                <a href="#">🔧 Help Center</a>
            </div>
            <p style="font-size: 12px; margin-top: 20px; color: #adb5bd;">
                This is an automated welcome message. Please do not reply to this email.<br>
                For assistance, contact our support team.
            </p>
        </div>
    </div>
</body>
</html>
            """
            
            # Attach both plain text and HTML versions
            msg.attach(MIMEText(text_body, 'plain'))
            msg.attach(MIMEText(html_body, 'html'))
            
            if self.smtp_config['use_tls']:
                server = smtplib.SMTP(self.smtp_config['server'], self.smtp_config['port'])
                server.starttls(context=ssl.create_default_context())
            else:
                server = smtplib.SMTP_SSL(self.smtp_config['server'], self.smtp_config['port'])
            
            server.login(self.smtp_config['username'], self.smtp_config['password'])
            text = msg.as_string()
            server.sendmail(self.smtp_config['username'], user_email, text)
            server.quit()
            
            return True
            
        except Exception as e:
            print(f"Error sending welcome email: {e}")
            return False
    
    def _get_current_date(self):
        """Get current date in a formatted string"""
        from datetime import datetime
        return datetime.now().strftime("%B %d, %Y")
