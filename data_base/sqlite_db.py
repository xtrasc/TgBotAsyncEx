import sqlite3 as sq
from create_b import bot,dp

def sql_start():
	global base, cur
	base = sq.connect("helper.db")
	cur = base.cursor()
	if base:
		print ("Data base good")
	base.execute("CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY)")
	base.commit()

	base.execute( "CREATE TABLE IF NOT EXISTS rasp(img TEXT)") 
	base.commit()

	base.execute( "CREATE TABLE IF NOT EXISTS met(img TEXT)") 
	base.commit()



async def sql_add_command(state):
	async with state.proxy() as data:
		cur.execute("INSERT INTO menu VALUES (?, ?)", tuple(data.values()))
		base.commit()

async def sql_read(message):
	for ret in cur.execute("SELECT * FROM menu").fetchall():
		await bot.send_photo(message.from_user.id, ret[0], f"{ret[1]}")


	