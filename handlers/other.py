from aiogram import types, Dispatcher
import string
from create_b import dp

@dp.message_handler()
async def echo_send(message : types.Message):
	await message.reply('Не то написал')
	
def register_handler_other(dp : Dispatcher):
	dp.register_message_handler(echo_send)