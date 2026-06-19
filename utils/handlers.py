from utils.decorators import access_checker
from utils.decorators import get_errors
import pyautogui
import keyboard
import subprocess

def setup_handlers(bot):

    @bot.message_handler(commands=["start"])
    @access_checker(bot)
    @get_errors(bot)
    def send_welcome(message):
        bot.send_message(message.chat.id, "<i>Добро пожаловать!</i>", parse_mode="HTML")

    @bot.message_handler(commands=["sleep", "s"])
    @access_checker(bot)
    @get_errors(bot)
    def go_sleep(message):
            bot.send_message(message.chat.id, "<i>Отправка ПК ко сну</i>", parse_mode="HTML")
            subprocess.run("rundll32.exe powrprof.dll,SetSuspendState 0,1,0", shell=True)
            bot.send_message(message.chat.id, "<i>ПК проснулся</i>", parse_mode="HTML")

    @bot.message_handler(commands=["poweroff", "po"])
    @access_checker(bot)
    @get_errors(bot)
    def go_out(message):
            bot.send_message(message.chat.id, "<i>Выключение ПК</i>", parse_mode="HTML")
            subprocess.run("shutdown /s /t 0", shell=True)

    @bot.message_handler(commands=["reboot", "r"])
    @access_checker(bot)
    @get_errors(bot)
    def go_reboot(message):
            bot.send_message(message.chat.id, "<i>Перезагрузка ПК</i>", parse_mode="HTML")
            subprocess.run("shutdown /r /t 0", shell=True)

    @bot.message_handler(commands=["screenshot", "ss"])
    @access_checker(bot)
    @get_errors(bot)
    def send_screenshot(message):
            screenshot = pyautogui.screenshot("image.png")
            bot.send_message(message.chat.id, "<i>Изображение создано</i>", parse_mode="HTML")
            with open('image.png', 'rb') as image:
                bot.send_photo(message.chat.id, image)
            subprocess.run("del image.png", shell=True)
            bot.send_message(message.chat.id, "<i>Изображение удалено</i>", parse_mode="HTML")

    @bot.message_handler(commands=["t"])
    @access_checker(bot)
    @get_errors(bot)
    def type_it(message):
        text = message.text
        text = text.removeprefix("/t")
        if text == "":
            bot.send_message(message.chat.id, "<i>Текст не указан</i>", parse_mode="HTML")
            return None
        else:
            text = text.removeprefix(" ")
            keyboard.write(text)
            bot.send_message(message.chat.id, "<i>Текст введен</i>", parse_mode="HTML")


    @bot.message_handler(commands=["kill"])
    @access_checker(bot)
    @get_errors(bot)
    def kill_task(message):
        text = message.text
        text = text.removeprefix("/kill")
        if text == "":
            bot.send_message(message.chat.id, "<i>Имя процесса не указано</i>", parse_mode="HTML")
            return None
        else:
            text = text.removeprefix(" ")
            bot.send_message(message.chat.id, f"<i>{subprocess.run(f"taskkill /im {text} /f", shell=True, text=True, encoding="cp866", capture_output=True).stdout}</i>", parse_mode="HTML")