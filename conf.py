import telebot
import os
from dotenv import load_dotenv
load_dotenv()

# Telegram botning tokeni
TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot("TOKEN")
