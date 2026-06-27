import sys
import subprocess
import importlib.metadata


def compile():
    import PyInstaller.__main__
    PyInstaller.__main__.run([
        'main.py',
        '--onefile',
        '--exclude-module=auto_installer',
        '--name=main'
    ])

def clear_console():
    if sys.platform.startswith('win'):
        subprocess.run("cls", shell=True)
    else:
        print("[-] Sorry, this script is only compatible with Windows.")
        sys.exit(1)

with open("requirements.txt", "r", encoding="UTF-16") as file:
    libs = file.read().splitlines()

not_installed_libs = []
installed_libs = []

for lib in libs:
    lib_name = lib.split('==')[0].split('>=')[0].strip()
    try:
        metadata = importlib.metadata.distribution(lib_name)
        installed_libs.append(lib_name)
    except importlib.metadata.PackageNotFoundError:
        not_installed_libs.append(lib_name)

clear_console()

print("Hello! It is auto installer for TelegramRemotePC.")
print("v 0.1.0")

def libs_checker():
    if len(not_installed_libs) >= 1:
        for lib in installed_libs:
            print(f"{lib} installed")
        for lib in not_installed_libs:
            print(f"{lib} not installed")
        print(f"\nInstaller found {len(not_installed_libs)} not installed libraries.")
        print("Would you like to install missing dependencies?")
        print("1. yes \n2. no ")
        choice = input(" > ")

        if choice == "1" or choice.lower() == "yes":
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
            except Exception as error:
                return "error"
            else:
                return "success"
        elif choice == "2" or choice.lower() == "no":
            print("\nExiting..")
            return "deny"
        else:
            clear_console()
            print("Incorrect choice.\nRestart the program..\nExiting..")
            return "error"
    else:
        return "success"

if libs_checker() == "success":
    pass
else:
    sys.exit()

clear_console()
print("All the dependencies are installed!")

clear_console()
print("Now you need to edit config.py")
print("We need to get your telegram Bot token.")
print("\nYou need to start @botfather bot at Telegram.")
print("Then type /newbot")
print("Then @botfather will ask you for an name and username for a Bot.")
print("After that, you will get your Telegram Bot token.")
print("Example: xxxxxxxxxx:YYYYYYYYYYYYYYYYYY")
print("\nNow, please input your token.")
TELEGRAM_BOT_TOKEN = input(" > ").strip()
print("Okay!")
clear_console()
print("Now we need to get your telegram user id.")
print("You can get it from @userinfobot by just pressing start.")
print("Example: 1234567890")
print("Please input your id.")
TELEGRAM_ID = input(" > ").strip()

with open("config.py", "w", encoding="utf-8") as config_file:
    config_file.write(f'TELEGRAM_BOT_TOKEN = "{TELEGRAM_BOT_TOKEN}"\n')
    config_file.write(f'TELEGRAM_ID = "{TELEGRAM_ID}"\n')

print("Are you ready to compile the project?")
print("1. Yes\n2. No")
choice = input(" > ").strip()

if choice == "1" or choice.lower() == "yes":
    try:
        compile()
        print("Compiled successfully!")
    except Exception as error:
        clear_console()
        print(error)