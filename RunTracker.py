import winreg

print("""
==============================
    Welcome to RunTracker! 🚀
==============================

Track your Applications. 

Connect with us:
[+] GitHub      : @AnonShade
[+] Twitter(X)  : @_AnonShade
""")


class AnonShade:
    def __init__(self):
        self.paths = {
            "HKEY_CURRENT_USER": [
                r"Software\Microsoft\Windows\CurrentVersion\Run",
                r"Software\Microsoft\Windows\CurrentVersion\RunOnce",
            ],
            "HKEY_LOCAL_MACHINE": [
                r"Software\Microsoft\Windows\CurrentVersion\Run",
                r"Software\Microsoft\Windows\CurrentVersion\RunOnce",
                r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Run",
            ],
        }
        self.apps = []

    def get_apps(self):
        for hive, paths in self.paths.items():
            for key_path in paths:
                try:
                    if hive == "HKEY_CURRENT_USER":
                        root = winreg.HKEY_CURRENT_USER
                    else:
                        root = winreg.HKEY_LOCAL_MACHINE

                    with winreg.OpenKey(root, key_path) as key:
                        i = 0
                        while True:
                            try:
                                name, value, _ = winreg.EnumValue(key, i)
                                self.apps.append((hive, key_path, name, value))
                                i += 1
                            except OSError:
                                break
                except FileNotFoundError:
                    continue

        return self.apps


startup_apps = AnonShade().get_apps()

if startup_apps:
    print(f"[?] Found : {len(startup_apps)} Apps\n")
    for hive, path, name, value in startup_apps:
        print(f"[+] Found in         : {hive}")
        print(f"[+] Registry Path    : {path}")
        print(f"[+] Application Name : {name}")
        print(f"[+] The Command      : {value}\n==========")
else:
    print("No startup applications found.")

input("\n\n\n[+] Enter To Exit")