from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from filters.test_filters import SomeFilter
from loader import dp


@dp.message_handler(CommandStart(), SomeFilter())
async def bot_start(message: types.Message, data_middleware, from_filter):
    await message.answer(f"Привет, {message.from_user.full_name}! \n{data_middleware=} \n{from_filter}")
