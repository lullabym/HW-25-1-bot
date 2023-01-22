import sqlite3
from config import bot2
import random

def sql_create() -> object:
    global db, cursor
    db = sqlite3.connect("bot.sqlite3")
    "="
    cursor = db.cursor()
    if db:
        print("База данных подключена!")

    db.execute("CREATE TABLE IF NOT EXISTS mentors "
               "(id INTEGER PRIMARY KEY AUTOINCREMENT, "
               "idm VARCHAR (255), "
               "name VARCHAR (255), "
               "dir VARCHAR (255), "
               "age INTEGER, "
               "groupm VARCHAR (255))")
    db.commit()

async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO mentors(idm, name, dir, age, groupm) VALUES"
                       " (?, ?, ?, ?, ?)", tuple(data.values()))
        db.commit()


async def sql_command_random(message):
    result = cursor.execute("SELECT * FROM mentors").fetchall()
    rand_ment = random.choice(result)
    await bot2.send_message(message.from_user.id,
        text=f"ID: {rand_ment[1]},\n"
             f"Name: {rand_ment[2]},\n"
             f"Direction: {rand_ment[3]},\n"
             f"Age:{rand_ment[4]},\n"
             f"Group:{rand_ment[5]}"
            )



async def sql_command_all():
    return cursor.execute("SELECT * FROM mentors").fetchall()


async def sql_command_delete(user_id):
    cursor.execute("DELETE FROM mentors WHERE id = ?", (user_id,))
    db.commit()