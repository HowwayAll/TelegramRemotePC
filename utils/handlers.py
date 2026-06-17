from utils.decorators import access_checker
import os
import pyautogui
import keyboard

def setup_handlers(bot):

    @bot.message_handler(commands=["start"])
    @access_checker
    def send_welcome(message):
        bot.send_message(message.chat.id, "<i>Добро пожаловать!</i>", parse_mode="HTML")

    @bot.message_handler(commands=["sleep", "s"])
    @access_checker
    def go_sleep(message):
            bot.send_message(message.chat.id, "<i>Отправка ПК ко сну</i>", parse_mode="HTML")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            bot.send_message(message.chat.id, "<i>ПК проснулся</i>", parse_mode="HTML")

    @bot.message_handler(commands=["poweroff", "po"])
    @access_checker
    def go_out(message):
            bot.send_message(message.chat.id, "<i>Выключение ПК</i>", parse_mode="HTML")
            os.system("shutdown /s /t 0")

    @bot.message_handler(commands=["reboot", "r"])
    @access_checker
    def go_reboot(message):
            bot.send_message(message.chat.id, "<i>Перезагрузка ПК</i>", parse_mode="HTML")
            os.system("shutdown /r /t 0")

    @bot.message_handler(commands=["screenshot", "ss"])
    @access_checker
    def send_screenshot(message):
            screenshot = pyautogui.screenshot("image.png")
            bot.send_message(message.chat.id, "<i>Изображение создано</i>", parse_mode="HTML")
            with open('image.png', 'rb') as image:
                bot.send_photo(message.chat.id, image)
            os.remove('image.png')
            bot.send_message(message.chat.id, "<i>Изображение удалено</i>", parse_mode="HTML")

    @bot.message_handler(commands=["t"])
    @access_checker
    def type_it(message):
        text = message.text
        text = text.removeprefix("/t")
        if text == "":
            return None
        else:
            text = text.removeprefix(" ")
            keyboard.write(text)
            bot.send_message(message.chat.id, "<i>Текст введен</i>", parse_mode="HTML")


    @bot.message_handler(commands=["kill"])
    @access_checker
    def kill_task(message):
        text = message.text
        text = text.removeprefix("/kill")
        if text == "":
            return None
        else:
            text = text.removeprefix(" ")
            os.system(f"taskkill /f /im {text}")