from aiogram import types, Dispatcher
from config import bot2, ADMINS

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


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!/')