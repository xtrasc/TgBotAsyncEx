from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_b import dp, bot
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove



class FSMAdmin(StatesGroup):
	photo = State()
	name = State()
	



@dp.message_handler(commands="Объявление", state=None)
async def cm_start(message : types.Message):
	await FSMAdmin.photo.set()
	await message.reply("Загрузи скрин/ фото изменений (если скрина нет загрузи что нибудь)")

async def load_photo(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data ["photo"] = message.photo[0].file_id
	await FSMAdmin.next()
	await message.reply("Напиши текстом что изменилось")

async def load_name(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data["name"] = message.text
	
	await sqlite_db.sql_add_command(state)
	await state.finish()

@dp.message_handler(state="*", commands="Отмена")
@dp.message_handler(Text(equals="Отмена", ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
	current_state = await state.get_state()
	if current_state is None:
		return
	await state.finish()
	await message.reply("ok")

def register_handler_admin(dp: Dispatcher):
	dp.register_message_handler(cm_start, commands=["Изменить"], state=None)
	dp.register_message_handler(load_photo, content_types=["photo"], state=FSMAdmin.photo)
	dp.register_message_handler(load_name, state=FSMAdmin.name)
	dp.register_message_handler(cancel_handler, state="*", commands="Отмена")
	dp.register_message_handler(cancel_handler, Text(equals='Отмена', ignore_case=True), state="*")