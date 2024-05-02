from conf import *
from telebot import types

courses = ["Front End 🙋", "Kompyuter savodxonlik 🙋"]
training_days = ["Du/Chor/Juma", "Se/Pay/Shan"]
training_time = ["10:00", "13:30", "15:00"]
user_data = {}


@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    msg = bot.reply_to(message, "Assalomu alaykum! Ismingizni kiriting:")
    bot.register_next_step_handler(msg, process_name_step)

@bot.message_handler(commands=['info'])
def send_info(message):
    chat_id = message.chat.id
    info_message = "Kompyuter savodxonlik\n Kurs davomida siz :\n Kompyuterdan foydalanish.\n Microsoft office dasturlaridan:\n―  Word;\n―  Excel;\n―  Power point va fayllar bilan ishlashni o’rganasiz.\n Kurs oxirida sertifikat beriladi!\n Kurs davomiyligi: 1 oy. Haftasiga 3 marta, 1.5 soat.\nKurs narxi: 250 000 so'm (bir oy uchun).\n\n Front-end dasturlash\nKurs davomida siz o’rganishingiz mumkin:\n―  Html\n―  Css\n―  Bootstrap\n―  JavaScript\n―  Vue.js\n―  Github\nKurs oxirida sertifikat beriladi!\nKurs davomida ko’plab loyixalar qilinadi.\nKurs davomiyligi: 8 oy. Haftasiga 3 marta, 1.5 soat.\nKurs narxi: 350 000 so'm (bir oy uchun).\nManzil: Shahrixon tumani Shahrixon shox ko'cha. Uztelecom binosi\nNomer +998941002434, +998951171024\nhttps://maps.app.goo.gl/gzFuTyA3NBpALMcm6?g_st=ic"
    bot.send_message(chat_id, info_message)

def is_valid_name(name):
    return name.isalpha()
def process_name_step(message):
    chat_id = message.chat.id
    name = message.text

    if is_valid_name(name):
        user_data[chat_id] = {"name": name}

        msg = bot.reply_to(message, "Telefon raqamingizni kiriting, Masalan 901234567:")
        bot.register_next_step_handler(msg, process_phone_step)
    else:
        msg = bot.reply_to(message, "Noto'g'ri format! Ismingizni faqat harflar bilan kiriting:")
        bot.register_next_step_handler(msg, process_name_step)

def validate_phone_number(phone):

    if phone.isdigit() and 9 <= len(phone) <= 12:
        return True
    else:
        return False    

def process_phone_step(message):
    chat_id = message.chat.id
    phone = message.text

    if validate_phone_number(phone):
        user_data[chat_id]["phone"] = phone
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        for course in courses:
            keyboard.add(types.KeyboardButton(course))

        msg = bot.reply_to(message, "Kursni tanlang:", reply_markup=keyboard)
        bot.register_next_step_handler(msg, process_course_step)
    else:
        msg = bot.reply_to(message, "Noto'g'ri telefon raqami formati. Iltimos, qayta kiriting:")
        bot.register_next_step_handler(msg, process_phone_step)

def process_course_step(message):
    chat_id = message.chat.id
    course = message.text
    user_data[chat_id]["course"] = course

    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    for day in training_days:
        keyboard.add(types.KeyboardButton(day))

    msg = bot.reply_to(message, "Kunni tanlang:", reply_markup=keyboard)
    bot.register_next_step_handler(msg, process_training_day_step)

def process_training_day_step(message):
    chat_id = message.chat.id
    training_day = message.text
    user_data[chat_id]["training_day"] = training_day

    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    for time in training_time:
        keyboard.add(types.KeyboardButton(time))

    msg = bot.reply_to(message, "Va soatni tanlang:", reply_markup=keyboard)
    bot.register_next_step_handler(msg, process_training_time_step)

def process_training_time_step(message):
    chat_id = message.chat.id
    training_time = message.text
    user_data[chat_id]["training_time"] = training_time

    name = user_data[chat_id]["name"]
    phone = user_data[chat_id]["phone"]
    course = user_data[chat_id]["course"]
    training_day = user_data[chat_id]["training_day"]
    training_time = user_data[chat_id]["training_time"]

    response = f"Foydalanuvchi: {name}\nTelefon: {phone}\nKurs: {course}\nKun: {training_day}\nSoat: {training_time}"
    admin_chat_id = "900490139"
    bot.send_message(admin_chat_id, response)
        
    bot.send_message(chat_id, "Tabriklayman, siz ro'yxatdan o'tdingiz!",
                     reply_markup=types.ReplyKeyboardRemove())

if __name__ == '__main__':
    while True:
        try:
            bot.polling()
        except Exception as e:
            print(e)
