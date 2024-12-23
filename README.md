
# 🚀 Startup Applications Manager

![Startup Applications Manager](https://github.com/user-attachments/assets/d0ba00fc-5d25-47cf-a935-a4f8dfc0d38f)

`RunTracker` is a lightweight tool designed to list all startup applications configured in the Windows registry. With this tool, you can easily view which applications are set to run at system startup, along with their details, all in one place. ✨

---

## 🌟 Features

- 🔍 **Fetch Startup Applications**: Retrieve startup programs registered in the Windows registry.
- 📂 **Detailed Information**:
  - 🗂️ Registry Hive
  - 📁 Registry Path
  - 🖥️ Application Name
  - 📜 Command/Path
- ✅ **Simple and Efficient**: Built-in functionality with no third-party dependencies.
- 🖥️ **Windows Only**: Optimized for Windows environments.

---

## 🖥️ Supported Devices

- **Operating Systems**: 🪟 Windows 10, Windows 11
- **Architecture**: x86 or x64
- **Python Version** (for source code): Python 3.6 or higher

---

## 📥 Download and Run

### **⬇️ Download the Executable (Recommended)**

1. Go to the [🚀 Releases](https://github.com/AnonShade/RunTracker/releases) section of this repository.
2. Download the latest `.exe` file for `RunTracker`.
3. Run the executable file—no installation required!

---

### **🐍 Run from Source Code**

#### **Steps**

1. Save the script file as `RunTracker.py`.
2. Open a terminal or command prompt and execute:
   ```bash
   python RunTracker.py
   ```
3. View the list of startup applications along with their details.

---

## 📖 Example Output

```
[?] Found : 3 Apps

- Found in         : HKEY_CURRENT_USER
- Registry Path    : Software\Microsoft\Windows\CurrentVersion\Run
- Application Name : MyApp
- The Command      : "C:\Program Files\MyApp\MyApp.exe"
==========

- Found in         : HKEY_LOCAL_MACHINE
- Registry Path    : Software\Microsoft\Windows\CurrentVersion\Run
- Application Name : AnotherApp
- The Command      : "C:\Program Files\AnotherApp\AnotherApp.exe"
==========

- Found in         : HKEY_LOCAL_MACHINE
- Registry Path    : SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Run
- Application Name : ThirdApp
- The Command      : "C:\ThirdApp\ThirdApp.exe"
==========
```

---

## 📝 Notes

- **Administrative Privileges**: Modifying or accessing some registry paths may require administrative privileges. Run the script or executable as an administrator if necessary.
- **Safety**: This script only reads registry entries and does not modify or delete them.
- **Compatibility**: Designed exclusively for Windows devices.

---

## 📜 License
This script is distributed under the MIT License. Feel free to use, modify, and distribute it as needed.

---
