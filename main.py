import asyncio

from aiogram.utils import executor
from config import dp, ADMINS, bot2
from handlers import client, callback, extra, admin, fsmAdminMentor, notification
import logging
from database.bot_db import sql_create


async def on_startup(_):
    asyncio.create_task(notification.scheduler())
    await bot2.send_message(chat_id=ADMINS[0],
                           text="Bot started!")
    sql_create()


client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
fsmAdminMentor.register_handlers_anketa(dp)
notification.register_handler_notification(dp)
# пустой handler нужно регистрировать последним
extra.register_handlers_extra(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True,
                           on_startup=on_startup)

