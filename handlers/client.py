from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot2, dp
from keyboards.client_kb import start_markup
from database.bot_db import sql_command_random

# @dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot2.send_message(message.from_user.id,
                            f"Привет, {message.from_user.full_name}!",
                            reply_markup=start_markup)
    # await message.answer("This is an answer method!")
    # await message.reply("This is a reply method!")

# @dp.message_handler(commands=['mem'])
async def mem(message: types.Message):
    photo = open("media/kiss.jpg", "rb")
    await bot2.send_photo(message.chat.id, photo=photo)


# @dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup1 = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton(
        "NEXT",
        callback_data="button_call_1"

    )
    markup1.add(button_call_1)

    question = "Какая страна производит больше всего кофе в мире?"
    answers = [
        "Бразилия",
        "Индонезия",
        "Колумбия"
    ]

    await bot2.send_poll(
        message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        open_period=5,
        reply_markup=markup1
    )

async def get_random_user(message: types.Message):
    await sql_command_random(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(mem, commands=['mem'])
    dp.register_message_handler(get_random_user, commands=['get'])

