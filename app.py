from aiogram import executor

from loader import dp, db
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from utils.db_api import gino_db


async def on_startup(dispatcher):
    print('Connect to db')
    await gino_db.on_startup(dp)
    print('clean db')
    await db.gino.drop_all()
    print('create table')
    await db.gino.create_all()
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
