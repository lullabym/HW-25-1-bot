from aiogram import types, Dispatcher
from config import bot2, dp
import random
from test import get_message


#@dp.message_handler()
async def echo(message: types.Message):
    emoji = '🏀 🎲 🎯 🎳 🎰'.split()
    erandom = random.choice(emoji)
    if message.text.isdigit():
        a = int(message.text)
        await message.answer(a ** 2)
    elif message.text.lower().startswith('game'):
        await bot2.send_dice(message.from_user.id, emoji=erandom)
    else:
        await message.answer(message.text)
    await message.answer(get_message(message))


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)