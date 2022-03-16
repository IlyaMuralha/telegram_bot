import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db
from utils.misc import rate_limit


@rate_limit(5, key='start')
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = await message.from_user.full_name
    # await message.answer(f"Привет, {message.from_user.full_name}!")
    await db.add_user(id=message.from_user.id, name=name)

    count = await db.count_users()
