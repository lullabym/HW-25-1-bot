from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ParseMode
from decouple import config
import markups
import logging

TOKEN = config("TOKEN")

bot2 = Bot(TOKEN)
dp = Dispatcher(bot=bot2)



@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
    await bot2.send_message(message.from_user.id,
                            f"Hi, {message.from_user.full_name}!")
    # await message.answer("This is an answer method!")
    # await message.reply("This is a reply method!")

@dp.message_handler(commands=['quiz'])
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
        open_period=10,
        reply_markup=markup1
    )

@dp.callback_query_handler(lambda func: func.data == "button_call_1")
async def quiz1(call: types.CallbackQuery):

    question = "Какой безалкогольный напиток был первым взят в космос?"
    answers = [
        "Пепси",
        "Кока-Кола",
        "Фанта"
    ]
    await bot2.send_poll(call.message.chat.id,
                        question=question,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=1,
                        open_period=10,
                        )

@dp.message_handler(commands=['mem'])
async def mem(message: types.Message):
    photo = open("media/kiss.jpg", "rb")
    await bot2.send_photo(message.chat.id, photo=photo)

@dp.message_handler()
async def echo_message(message: types.Message):
    if message.text.isdigit():
        a = int(message.text)
        await message.answer(a ** 2)
    else:
        await message.answer(message.text)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)

