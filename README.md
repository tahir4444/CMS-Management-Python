# Enterprise CMS - Professional Customer Management

[![Status](https://img.shields.io/badge/Status-Ready%20to%20Use-brightgreen)](https://github.com/yourusername/enterprise-cms)
[![Platform](https://img.shields.io/badge/Platform-Windows-blue)](https://www.microsoft.com/windows)
[![Python](https://img.shields.io/badge/Python-3.8+-yellow)](https://www.python.org/)

> **Enterprise-grade Customer Management System with professional design and responsive layout**

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [System Requirements](#system-requirements)
- [Quick Start](#quick-start)
- [Installation & Usage](#installation--usage)
- [Development](#development)
- [Troubleshooting](#troubleshooting)
- [File Structure](#file-structure)

## 🎯 Overview

**Enterprise CMS** is a professional, enterprise-grade Customer Management System built with Python and Tkinter. It features a modern, responsive design that adapts to any window size, secure user authentication, and comprehensive customer data management.

### ✨ Key Highlights

- 🎨 **Professional Enterprise Design** - Modern UI with professional color scheme
- 📱 **Fully Responsive** - Adapts to any window size automatically
- 🔒 **Secure Authentication** - SHA-256 password hashing
- 💾 **Local Database** - SQLite3 for data persistence
- 🚀 **Standalone Executable** - No Python installation required for end users

## 🎨 Features

### Core Functionality
- **User Registration & Login System**
  - Secure customer registration with validation
  - Professional login interface
  - **Email-based password recovery system**
  - **Remember me functionality**
  - **Saved credentials management**

- **Customer Dashboard**
  - Personalized user dashboard
  - Navigation between different sections
  - User information display

- **User Management**
  - Complete users listing
  - Advanced search functionality
  - CSV export capabilities
  - User statistics

### Technical Features
- **Modern UI/UX**
  - Professional color palette
  - Responsive grid layout
  - Custom message dialogs
  - Professional typography (Inter font family)

- **Security**
  - SHA-256 password hashing
  - Input validation
  - Secure database operations

- **Performance**
  - Efficient SQLite database
  - Optimized UI rendering
  - Responsive design updates

## 💻 System Requirements

### Minimum Requirements
- **Operating System**: Windows 10/11 (64-bit)
- **Memory**: 4 GB RAM
- **Storage**: 100 MB free space
- **Display**: 800x600 minimum resolution

### Development Requirements
- **Python**: 3.8 or higher
- **SQLite3**: Built-in with Python
- **Additional Packages**: PyInstaller (for exe creation)

## 🚀 Quick Start

### Option 1: Desktop Shortcut (Recommended)
1. Double-click "Customer Management System" on your desktop
2. ✅ Custom icon will show in taskbar

### Option 2: Start Menu
1. Press Windows key
2. Type "Customer Management System"
3. Click on the app
4. ✅ Custom icon will show in taskbar

### Option 3: Batch File
1. Double-click `run_cms.bat`
2. ✅ Custom icon will show in taskbar

### Option 4: Direct Executable
1. Navigate to `dist` folder
2. Double-click `CustomerManagementSystem.exe`
3. ✅ Custom icon will show in taskbar

### Option 5: Python Script (Development)
```bash
python main.py
```
⚠️ **Note**: Will show Python icon in taskbar

## 📧 SMTP Setup (For Password Reset Emails)

### Configure Email Service
1. **✅ Already Configured** - Brevo SMTP settings are ready to use
2. **Test** the password reset functionality by clicking "Forgot your password?"
3. **Optional** - Edit `smtp_config.py` to use a different email provider

### Supported Email Providers
- **Brevo (Sendinblue)** - Configured and ready to use
- **Gmail** - Use App Password
- **Outlook/Hotmail** - Use App Password
- **Yahoo** - Use App Password
- **Custom SMTP** - Contact your provider

### Brevo Setup Example (Currently Configured)
```python
SMTP_CONFIG = {
    'server': 'smtp-relay.brevo.com',
    'port': 587,
    'username': '902a84002@smtp-brevo.com',
    'password': 'your-brevo-api-key',
    'use_tls': True
}
```

⚠️ **Security**: Never commit real credentials to version control!

## 📦 Installation & Usage

### First-Time Setup
1. **Download** the application files
2. **Extract** to your desired folder
3. **Run** the executable or create shortcuts
4. **Register** your first account
5. **Login** and start managing customers

### Creating Shortcuts
- **Desktop Shortcut**: Use `create_desktop_shortcut.py`
- **Start Menu**: Use `create_desktop_shortcut.py`
- **Batch File**: Use `run_cms.bat`

## 🔧 Development

### Prerequisites
```bash
# Install required packages
pip install pyinstaller
pip install pillow  # For icon creation
```

### Project Structure
```
enterprise-cms/
├── main.py                 # Main application source code
├── create_exe.py          # Script to regenerate executable
├── create_icon.py         # Icon creation utility
├── create_desktop_shortcut.py  # Shortcut creation
├── run_cms.bat            # Batch file launcher
├── launch_cms.py          # Python launcher
├── app_icon.ico           # Application icon
├── app_icon.png           # PNG icon version
├── app_icon_small.png     # Small PNG icon
├── customers.db           # SQLite database (auto-created)
├── dist/                  # Generated executable folder
│   └── CustomerManagementSystem.exe
└── README.md              # This file
```

### Modifying the Application
1. **Edit** `main.py` with your changes
2. **Test** with `python main.py`
3. **Regenerate** executable: `python create_exe.py`
4. **Distribute** the new exe file

## 🔄 Regenerating the Executable

### Method 1: Automated Script (Recommended)
```bash
python create_exe.py
```
- Automatically installs PyInstaller if needed
- Creates executable with custom icon
- Places result in `dist/` folder

### Method 2: Manual PyInstaller
```bash
# Install PyInstaller
pip install pyinstaller

# Create executable
pyinstaller --onefile --windowed --icon=app_icon.ico --name=CustomerManagementSystem main.py
```

### Method 3: Step-by-Step
```bash
# 1. Install PyInstaller
pip install pyinstaller

# 2. Create executable
pyinstaller --onefile --windowed --icon=app_icon.ico --name=CustomerManagementSystem main.py

# 3. Find executable in dist/ folder
```

⚠️ **Important**: Always regenerate the exe file after making changes to `main.py`!

## 🔍 Troubleshooting

### Common Issues

#### Executable Won't Run
1. **Check Version**: Ensure latest exe: `python create_exe.py`
2. **File Location**: Verify all files are in the same folder
3. **Permissions**: Try running as administrator
4. **Antivirus**: Check if Windows Defender is blocking the file

#### Missing Module Errors
1. **Install PyInstaller**: `pip install pyinstaller`
2. **Check Directory**: Ensure you're in the project folder
3. **Verify Imports**: Check `main.py` for import errors

#### Icon Not Displaying
1. **Regenerate Exe**: `python create_exe.py`
2. **Check Icon Files**: Ensure `app_icon.ico` exists
3. **Clear Cache**: Restart Explorer if needed

### Error Messages

| Error | Solution |
|-------|----------|
| "Missing module" | Install PyInstaller: `pip install pyinstaller` |
| "Permission denied" | Run as administrator |
| "File not found" | Check file paths and regenerate exe |
| "Icon not loading" | Verify icon files exist and regenerate exe |

## 📁 File Structure

### Core Files
- **`main.py`** - Main application source code
- **`create_exe.py`** - Executable generation script
- **`customers.db`** - SQLite database (auto-created)

### Executables & Launchers
- **`dist/CustomerManagementSystem.exe`** - Main application
- **`run_cms.bat`** - Batch file launcher
- **`launch_cms.py`** - Python launcher script

### Icons & Assets
- **`app_icon.ico`** - Windows icon file
- **`app_icon.png`** - PNG icon version
- **`app_icon_small.png`** - Small PNG for taskbar

### Utilities
- **`create_icon.py`** - Icon creation utility
- **`create_desktop_shortcut.py`** - Shortcut creation
- **`view_database.py`** - Database viewer utility

## 🤝 Contributing

### Development Workflow
1. **Fork** the repository
2. **Create** feature branch
3. **Make** your changes
4. **Test** thoroughly
5. **Submit** pull request

### Code Style
- Follow PEP 8 guidelines
- Add comments for complex logic
- Maintain consistent naming conventions
- Test all changes before submitting

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Tkinter** - GUI framework
- **SQLite3** - Database engine
- **PyInstaller** - Executable creation
- **Pillow** - Image processing

## 📞 Support

### Getting Help
- **Documentation**: Check this README first
- **Issues**: Report bugs via GitHub issues
- **Questions**: Open a discussion for help

### Common Questions

**Q: How do I change the application icon?**
A: Edit `create_icon.py` and regenerate the exe file.

**Q: Can I modify the database structure?**
A: Yes, edit the SQL commands in `main.py` and regenerate the exe.

**Q: How do I add new features?**
A: Modify `main.py`, test with Python, then regenerate the exe.

---

## 🎉 Ready to Use!

Your **Enterprise Customer Management System** is now ready with:
- ✅ Professional enterprise design
- ✅ Responsive layout
- ✅ Secure authentication
- ✅ Custom icon support
- ✅ Standalone executable
- ✅ Comprehensive documentation

**Start managing your customers professionally today!** 🚀

---

*Last updated: December 2024*
*Version: 2.0 - Enterprise Edition*
