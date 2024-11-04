from aiogram import types, Dispatcher
from create_b import dp, bot
from keyboards import kb_client, rall
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup
from aiogram.dispatcher.filters import Text

	

@dp.message_handler(commands=["start","help"])
async def command_start(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, "Привет, данный бот является проектом и был создан для облегчения учебного процесса", reply_markup=kb_client)
		await message.delete()
		user_id=message.from_user.id
	except:
		await message.reply("к")


@dp.message_handler(commands=["Преподаватели"])
async def teacher_timetable_command(message: types.Message):
	kb1 = [
		[
			types.KeyboardButton(text="Кузьмин В.С."),
			types.KeyboardButton(text="Стряпкин Л.И."),
			types.KeyboardButton(text="Лызлов С.С."),
			types.KeyboardButton(text="Антонов А.А.")
		]
	]

	keyboard=types.ReplyKeyboardMarkup(
		keyboard=kb1,
		resize_keyboard=True
	)
	await message.answer ("Выбери расписание какого преподавателя ты хочешь посмотреть", reply_markup=keyboard)
@dp.message_handler(text=["Кузьмин В.С."])
async def  teacher_timetable_command(message: types.Message):
	await message.reply("Пятница 8:30-9:50 4401| 10:05-11:25 4325|Понедельник 13:45-15:05 4224")

@dp.message_handler(text=["Стряпкин Л.И."])
async def  teacher_timetable_command(message: types.Message):
	await message.reply("Пятница 8:30-9:50 2424| 10:05-11:25 2201 \nПонедельник 13:45-15:05 3101")

@dp.message_handler(text=["Лызлов С.С."])
async def  teacher_timetable_command(message: types.Message):
	await message.reply("Пятница 8:30-9:50 2424| 10:05-11:25 2431 \nПонедельник 13:45-15:05 4405")

@dp.message_handler(text=["Антонов А.А."])
async def  teacher_timetable_command(message: types.Message):
	await message.reply("Пятница 13:45-15:05 4101| 15:20-16:40 4225 \nПонедельник 13:45-15:05 4201")

@dp.message_handler(commands=["Обучение"])
async def study_material_command(message: types.Message):
	kb2 = [
		[
			types.KeyboardButton(text="Уроки по маткаду"),
			types.KeyboardButton(text="Уроки по мультисим"),
			types.KeyboardButton(text="Собранные методические материалы по учебе на семестр")
		]
	]
	keyboard=types.ReplyKeyboardMarkup(
		keyboard=kb2,
		resize_keyboard=True
	)
	await message.answer ("В чем у тебя затруднения?", reply_markup=keyboard)
@dp.message_handler(text=["Уроки по маткаду"])
async def  study_material_command(message: types.Message):
	await message.reply("https://www.youtube.com/watch?v=J4ysQ5i6PCA&ab_channel=SardorJumaniyozov")

@dp.message_handler(text=["Уроки по мультисим"])
async def  study_material_command(message: types.Message):
	await message.reply("https://www.youtube.com/watch?v=1sa_oMOoOrY&ab_channel=%D0%9F%D0%B0%D1%8F%D0%BB%D1%8C%D0%BD%D0%B8%D0%BATV")

@dp.message_handler(text=["Собранные методические материалы по учебе на семестр"])
async def  study_material_command(message: types.Message):
	await message.reply("https://disk.yandex.ru/d/3kAHxDGJmAAiJQ")



@dp.message_handler(commands=['Расписание'])
async def student_timetable_command(message: types.Message):
	kb3 = [
		[
			types.KeyboardButton(text="На сегодня"),
			types.KeyboardButton(text="Общее")
		]
	]
	keyboard=types.ReplyKeyboardMarkup(
		keyboard=kb3,
		resize_keyboard=True
	)
	await message.answer ("Выбери какое", reply_markup=keyboard)
@dp.message_handler(text=["На сегодня"])
async def  student_timetable_command(message: types.Message):
	await message.reply("Сегодня Понедельник\n 8:30-9:50 Правовая культура Гоц Е.В. 4518\n 10:05-11:25 Полупроводниковая схемотехника Лызлов С.С. 4534")

@dp.message_handler(text=["Общее"])
async def  student_timetable_command(message: types.Message):
	await message.reply("https://1drv.ms/i/s!Anrq5LVa6_hZwH0va-uY-JQ1Yv-7?e=Gy9ERi")


@dp.message_handler(commands=["Инфо"])
async def photo_up_command(message: types.Message):
	await sqlite_db.sql_read(message)


def register_handler_clinet(dp: Dispatcher):
	dp.register_message_handler(command_start, commands=["start","help"])
	dp.register_message_handler(teacher_timetable_command, commands=["Преподаватели"])
	dp.register_message_handler(study_material_command, commands=["Обучение"])
	dp.register_message_handler(student_timetable_command, commands=["Расписание"])
	dp.register_message_handler(photo_up_command, commands=["Инфо"])
	