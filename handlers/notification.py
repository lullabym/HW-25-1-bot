import aioschedule
import time
from aiogram import types, Dispatcher
from config import bot2
import asyncio

async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = []
    chat_id.append(message.from_user.id)
    await message.answer("Ok")

async def rent():
    photo = open('media/rentmem.jpg', 'rb')
    for id in chat_id:
        await bot2.send_photo(id, photo=photo, caption="Всё ещё нужна крыша над головой?"
                                                    " Тогда готовь кошелёк, ведь хозяйка ждёт.")

async def scheduler():
        aioschedule.every().monday.at('10:00').do(rent)
        while True:
            await aioschedule.run_pending()
            await asyncio.sleep(1)



def register_handler_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id, lambda word: 'напомни' in word.text)
