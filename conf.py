import telebot
import os
from dotenv import load_dotenv
load_dotenv()

# Telegram botning tokeni
TOKEN = os.getenv("TOKEN")
# Botni tokenini kiriting
bot = telebot.TeleBot("TOKEN")
