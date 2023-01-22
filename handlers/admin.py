import random
from aiogram import types, Dispatcher
from config import bot2, ADMINS
from database.bot_db import sql_command_all, sql_command_delete
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def pin(message: types.Message):
    if message.chat.type != "private":
        if message.from_user.id not in ADMINS:
            await message.answer("Вы не являетесь администратором.")
        elif not message.reply_to_message:
            await message.answer("Команда должна быть ответом на сообщение!")
        else:
            await bot2.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    else:
        await message.answer("Пишите в группу.")


async def delete_data(message: types.Message):
    if message.from_user.id not in ADMINS:
        await message.answer("Ты не мой босс!")
    else:
        users = await sql_command_all()
        rand_ment = random.choice(users)
        await bot2.send_message(message.from_user.id,
        text=f"ID: {rand_ment[1]},\n"
             f"Name: {rand_ment[2]},\n"
             f"Direction: {rand_ment[3]},\n"
             f"Age:{rand_ment[4]},\n"
             f"Group:{rand_ment[5]}",
              reply_markup=InlineKeyboardMarkup().add(
                InlineKeyboardButton(f"delete {rand_ment[2]}",
                 callback_data=f"delete {rand_ment[2]}")))


async def complete_delete(call: types.CallbackQuery):
    await sql_command_delete(call.data.replace("delete ", ""))
    await call.answer(text="Удалено", show_alert=True)
    await bot2.delete_message(call.from_user.id, call.message.message_id)

def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!/')
    dp.register_message_handler(delete_data, commands=['del'])
    dp.register_callback_query_handler(complete_delete,
                                       lambda call: call.data and call.data.startswith("delete "))
