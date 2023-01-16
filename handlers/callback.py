from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot2, dp

#@dp.callback_query_handler(lambda func: func.data == "button_call_1")
async def quiz_2(call: types.CallbackQuery):
    markup2 = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton(
        "NEXT",
        callback_data="button_call_2"
    )
    markup2.add(button_call_2)

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
                        open_period=5,
                        reply_markup=markup2
                        )

#@dp.callback_query_handler(lambda func: func.data == "button_call_2")
async def quiz_3(call: types.CallbackQuery):
    markup3 = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton(
        "NEXT",
        callback_data="button_call_3"
    )
    markup3.add(button_call_3)

    question = "Сколько сердец у осьминога?"
    answers = [
        "1",
        "2",
        "3"
    ]
    await bot2.send_poll(call.message.chat.id,
                        question=question,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=2,
                        open_period=5,
                        reply_markup=markup3
                        )

#@dp.callback_query_handler(lambda func: func.data == "button_call_3")
async def quiz_4(call: types.CallbackQuery):
    question = "Кто из этих персонажей не дружит с Гарри Поттером?"
    answers = [
        "Рон Уизли",
        "Драко Малфой",
        "Хагрид"
    ]
    await bot2.send_poll(call.message.chat.id,
                        question=question,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=1,
                        open_period=5,
                        )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="button_call_1")
    dp.register_callback_query_handler(quiz_3, text="button_call_2")
    dp.register_callback_query_handler(quiz_4, text="button_call_3")