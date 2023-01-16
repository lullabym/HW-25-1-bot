from aiogram import Bot, Dispatcher
from decouple import config

TOKEN = config("TOKEN")

bot2 = Bot(TOKEN)
dp = Dispatcher(bot=bot2)
ADMINS = (887976765, )