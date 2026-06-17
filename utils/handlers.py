from utils.decorators import access_checker
from utils.decorators import error_catcher
from data.langs import LANGS
import os
import pyautogui
import keyboard

def setup_handlers(bot):

    def get_text(message, key):
     user_lang = message.from_user.language_code
     lang_pack = LANGS.get(user_lang, LANGS['en'])
     return lang_pack.get(key, "Error: missing text / check dictionary")

    @bot.message_handler(commands=["start"])
    @access_checker
    def send_welcome(message):
        text = get_text(message, "granted")
        bot.send_message(message.chat.id, text, parse_mode="HTML")

    @bot.message_handler(commands=["sleep", "s"])
    @access_checker
    @error_catcher
    def go_sleep(message):
            text = get_text(message, "granted")
            bot.send_message(message.chat.id, text, parse_mode="HTML")
            text = get_text(message, "sleep")
            bot.send_message(message.chat.id, text, parse_mode="HTML")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            text = get_text(message, "wakeup")
            bot.send_message(message.chat.id, text, parse_mode="HTML")

    @bot.message_handler(commands=["poweroff", "po"])
    @access_checker
    @error_catcher
    def go_out(message):
            text = get_text(message, "granted")
            bot.send_message(message.chat.id, text, parse_mode="HTML")
            text = get_text(message, "turnoff")
            bot.send_message(message.chat.id, text, parse_mode="HTML")
            os.system("shutdown /s /t 0")

    @bot.message_handler(commands=["reboot", "r"])
    @access_checker
    @error_catcher
    def go_reboot(message):
            text = get_text(message, "granted")
            bot.send_message(message.chat.id, text, parse_mode="HTML")
            text = get_text(message, "reboot")
            bot.send_message(message.chat.id, text, parse_mode="HTML")
            os.system("shutdown /r /t 0")

    @bot.message_handler(commands=["screenshot", "ss"])
    @access_checker
    @error_catcher
    def send_screenshot(message):
            text = get_text(message, "granted")
            bot.send_message(message.chat.id, text, parse_mode="HTML")
            screenshot = pyautogui.screenshot("image.png")
            text = get_text(message, "image_created")
            bot.send_message(message.chat.id, text, parse_mode="HTML")
            with open('image.png', 'rb') as image:
                bot.send_photo(message.chat.id, image)
            os.remove('image.png')
            text = get_text(message, "image_deleted")
            bot.send_message(message.chat.id, text, parse_mode="HTML")

    @bot.message_handler(commands=["t"])
    @access_checker
    @error_catcher
    def type_it(message):
        text = message.text
        text = text.removeprefix("/t")
        if text == "":
            return None
        else:
            text = text.removeprefix(" ")
            keyboard.write(text)


    @bot.message_handler(commands=["kill"])
    @access_checker
    @error_catcher
    def kill_task(message):
        text = message.text
        text = text.removeprefix("/kill")
        if text == "":
            return None
        else:
            text = text.removeprefix(" ")
            os.system(f"taskkill /f /im {text}")