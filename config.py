from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

TOKEN = config("TOKEN")

bot2 = Bot(TOKEN)
dp = Dispatcher(bot=bot2, storage=storage)
ADMINS = (887976765, )