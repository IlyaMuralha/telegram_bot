from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, data_middleware):
    await message.answer(f"Привет, {message.from_user.full_name}! \n{data_middleware=}")
