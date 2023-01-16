# from aiogram import Bot, Dispatcher, types
# from aiogram.utils import executor
# from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ParseMode
# from decouple import config
# import markups
# import logging
# import random
#
# TOKEN = config("TOKEN")
#
# bot2 = Bot(TOKEN)
# dp = Dispatcher(bot=bot2)
#
#
#
# @dp.message_handler(commands=['start'])
# async def echo(message: types.Message):
#     await bot2.send_message(message.from_user.id,
#                             f"Hi, {message.from_user.full_name}!")
#
#
# @dp.message_handler(commands=['quiz'])
# async def quiz_1(message: types.Message):
#     markup1 = InlineKeyboardMarkup()
#     button_call_1 = InlineKeyboardButton(
#         "NEXT",
#         callback_data="button_call_1"
#     )
#     markup1.add(button_call_1)
#
#     question = "Какая страна производит больше всего кофе в мире?"
#     answers = [
#         "Бразилия",
#         "Индонезия",
#         "Колумбия"
#     ]
#
#     await bot2.send_poll(
#         message.from_user.id,
#         question=question,
#         options=answers,
#         is_anonymous=False,
#         type='quiz',
#         correct_option_id=0,
#         open_period=5,
#         reply_markup=markup1
#     )
#
# @dp.callback_query_handler(lambda func: func.data == "button_call_1")
# async def quiz_2(call: types.CallbackQuery):
#     markup2 = InlineKeyboardMarkup()
#     button_call_2 = InlineKeyboardButton(
#         "NEXT",
#         callback_data="button_call_2"
#     )
#     markup2.add(button_call_2)
#
#     question = "Какой безалкогольный напиток был первым взят в космос?"
#     answers = [
#         "Пепси",
#         "Кока-Кола",
#         "Фанта"
#     ]
#     await bot2.send_poll(call.message.chat.id,
#                         question=question,
#                         options=answers,
#                         is_anonymous=False,
#                         type='quiz',
#                         correct_option_id=1,
#                         open_period=5,
#                         reply_markup=markup2
#                         )
#
# @dp.callback_query_handler(lambda func: func.data == "button_call_2")
# async def quiz_3(call: types.CallbackQuery):
#     markup3 = InlineKeyboardMarkup()
#     button_call_3 = InlineKeyboardButton(
#         "NEXT",
#         callback_data="button_call_3"
#     )
#     markup3.add(button_call_3)
#
#     question = "Сколько сердец у осьминога?"
#     answers = [
#         "1",
#         "2",
#         "3"
#     ]
#     await bot2.send_poll(call.message.chat.id,
#                         question=question,
#                         options=answers,
#                         is_anonymous=False,
#                         type='quiz',
#                         correct_option_id=2,
#                         open_period=5,
#                         reply_markup=markup3
#                         )
#
# @dp.callback_query_handler(lambda func: func.data == "button_call_3")
# async def quiz_4(call: types.CallbackQuery):
#     question = "Кто из этих персонажей не дружит с Гарри Поттером?"
#     answers = [
#         "Рон Уизли",
#         "Драко Малфой",
#         "Хагрид"
#     ]
#     await bot2.send_poll(call.message.chat.id,
#                         question=question,
#                         options=answers,
#                         is_anonymous=False,
#                         type='quiz',
#                         correct_option_id=1,
#                         open_period=5,
#                         )
#
#
# @dp.message_handler(commands=['mem'])
# async def mem(message: types.Message):
#     photo = open("media/kiss.jpg", "rb")
#     await bot2.send_photo(message.chat.id, photo=photo)
#
#
# @dp.message_handler()
# async def echo_message(message: types.Message):
#     emoji = '🏀 🎲 🎯 🎳 🎰'.split()
#     erandom = random.choice(emoji)
#     if message.text.isdigit():
#         a = int(message.text)
#         await message.answer(a ** 2)
#     elif message.text.lower().startswith('game'):
#         await bot2.send_dice(message.from_user.id, emoji=erandom)
#     else:
#         await message.answer(message.text)
#
#
#
# if __name__ == '__main__':
#     logging.basicConfig(level=logging.INFO)
#     executor.start_polling(dp, skip_updates=True)
#
