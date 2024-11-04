import aiogram
from aiogram.utils import executor
from create_b import dp
from data_base import sqlite_db




async def on_startup(_):
	print("On")
	sqlite_db.sql_start()


from handlers import clinet, admin, other

clinet.register_handler_clinet(dp)
admin.register_handler_admin(dp)
other.register_handler_other(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

