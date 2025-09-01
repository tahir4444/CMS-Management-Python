# 🏢 Enterprise CMS - Professional Customer Management System

A modern, professional Windows application built with Python and Tkinter for comprehensive customer management.

## 🚀 Features

- **🔐 Secure Authentication**: Login/Registration with password hashing
- **💾 Remember Me**: Save credentials for convenience
- **📧 Password Reset**: Email-based password recovery
- **📊 Dynamic Dashboard**: Real-time statistics and recent activity
- **👥 User Management**: Complete CRUD operations for customers
- **📧 Welcome Emails**: Professional email templates for new registrations
- **🎨 Professional UI**: Modern, responsive design with Material Design principles
- **🔧 Modular Architecture**: Scalable, maintainable codebase
- **📦 Standalone Executable**: Easy distribution with PyInstaller

## 🛠️ Technology Stack

- **Frontend**: Tkinter, ttk (Themed Tkinter)
- **Backend**: Python 3.8+
- **Database**: SQLite3 (development), PostgreSQL (production recommended)
- **Email Service**: SMTP (Brevo/Sendinblue)
- **Build Tool**: PyInstaller
- **Version Control**: Git

## 📋 Prerequisites

- Python 3.8 or higher
- Git (for version control)
- SMTP service account (Brevo, Gmail, etc.)

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/tahir4444/CMS-Management-Python.git
cd CMS-Management-Python
```

### 2. Set Up Virtual Environment
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
# or
source .venv/bin/activate  # Linux/Mac
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure SMTP Settings
```bash
# Copy the template file
copy smtp_config_template.py smtp_config.py
# Edit smtp_config.py with your actual SMTP credentials
```

### 5. Run the Application
```bash
python main.py
```

## 🔧 Configuration

### SMTP Configuration
1. Copy `smtp_config_template.py` to `smtp_config.py`
2. Update the configuration with your SMTP credentials:
   ```python
   SMTP_CONFIG = {
       'server': 'smtp-relay.brevo.com',
       'port': 587,
       'username': 'your_username@smtp-brevo.com',
       'password': 'your_smtp_password',
       'use_tls': True,
       'sender_email': 'your_verified_email@gmail.com',
       'sender_name': 'CMS System'
   }
   ```

### Database Configuration
- **Development**: SQLite3 (automatic)
- **Production**: PostgreSQL (recommended)

## 📦 Building Executable

### Create Standalone Executable
```bash
python create_exe.py
```

### Run the Executable
```bash
# Windows
dist\CustomerManagementSystem.exe

# Or use the batch file
run_cms.bat
```

## 🏗️ Project Structure

```
Enterprise-CMS/
├── src/
│   └── cms/
│       ├── core/           # Application core
│       ├── config/         # Configuration files
│       ├── services/       # Business logic services
│       ├── ui/            # User interface components
│       ├── models/        # Data models
│       └── utils/         # Utility functions
├── assets/               # Static assets (icons, images)
├── dist/                # Built executables
├── main.py              # Application entry point
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## 🔐 Security Features

- **Password Hashing**: SHA-256 encryption
- **Credential Storage**: Secure local storage
- **Input Validation**: Comprehensive validation for all inputs
- **SQL Injection Protection**: Parameterized queries
- **Sensitive Data Protection**: Configuration templates

## 📧 Email Features

- **Welcome Emails**: Professional HTML templates for new users
- **Password Reset**: Secure email-based password recovery
- **SMTP Integration**: Support for multiple email providers

## 🎨 UI/UX Features

- **Responsive Design**: Adapts to different window sizes
- **Professional Styling**: Modern Material Design principles
- **Custom Dialogs**: Professional message boxes and modals
- **Intuitive Navigation**: Easy-to-use interface
- **Accessibility**: Keyboard shortcuts and clear labeling

## 🗄️ Database Features

- **User Management**: Complete CRUD operations
- **Search & Filter**: Advanced user search capabilities
- **Export Functionality**: CSV export for user data
- **Activity Tracking**: Recent activity monitoring
- **Statistics**: Dynamic dashboard statistics

## 🚀 Deployment

### Development
```bash
python main.py
```

### Production
1. Build executable: `python create_exe.py`
2. Distribute: `dist/CustomerManagementSystem.exe`
3. Configure SMTP settings
4. Set up production database (PostgreSQL recommended)

## 🔧 Development

### Adding New Features
1. Follow the modular architecture
2. Add tests for new functionality
3. Update documentation
4. Follow coding standards

### Code Style
- Use meaningful variable names
- Add docstrings to functions
- Follow PEP 8 guidelines
- Use type hints where appropriate

## 🐛 Troubleshooting

### Common Issues

**Application won't start**
- Check Python version (3.8+ required)
- Verify virtual environment is activated
- Check for missing dependencies

**Email not working**
- Verify SMTP credentials in `smtp_config.py`
- Check sender email verification
- Test SMTP connection with `test_email.py`

**Database issues**
- Check file permissions for SQLite database
- Verify database path in settings
- Run `add_demo_users.py` to populate test data

**Icon not displaying**
- Regenerate icons: `python create_icon.py`
- Rebuild executable: `python create_exe.py`
- Clear Windows icon cache

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📞 Support

For support and questions:
- Create an issue on GitHub
- Check the troubleshooting section
- Review the documentation

## 🔄 Version History

- **v1.0.0**: Initial release with core functionality
- **v1.1.0**: Added email features and professional UI
- **v1.2.0**: Modular architecture and enhanced security
- **v1.3.0**: Git integration and deployment improvements

---

**Built with ❤️ using Python and Tkinter**
