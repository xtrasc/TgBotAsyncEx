from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton

b1= KeyboardButton('/Расписание')
b2= KeyboardButton('/Преподаватели')
b3= KeyboardButton('/Обучение')
b4= KeyboardButton('/Объявление')
b5= KeyboardButton('/Инфо')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).row(b2, b3).add(b4).add(b5)


rall= InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text="Полное расписание", callback_data=""))

