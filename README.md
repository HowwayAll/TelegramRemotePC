# telegram-remote-pc
# telegram-bot

> [!TIP]
> I AM STILL WORKING ON THIS PROJECT. BUT YOU CAN STILL USE IT.

This Python script can give you access to control your PC from a Telegram Bot.

## Features

- **Turn Off PC**
- **Reboot PC**
- **Send PC to sleep**
- **Get screenshot and send it**
- **Type something (pressing buttons)**
- **Kill the process**
- **Execute a command**
- **Easy to install**
- **Tested on Windows 11**
- **100% functional on Windows 11**

## Prerequisites

- Python 3.6 or higher
- Windows 11 operating system

## Installation

1. Clone this repository or download the scripts:

    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Create config.py near the main.py

    ```bash
    echo TOKEN="xxxxxxxxxxxxx:XXXXXXXXXXXXXXX" > config.py
    ```
    get token from @botfather
    ```bash
    echo TELEGRAM_ID=1234567890 >> config.py
    ```
    get id from @userinfobot

4. Compile your project

    ```bash
    pyinstaller --onefile main.py
    ```
 
## License
**This project is licensed under the MIT License - see the LICENSE file for details.**
