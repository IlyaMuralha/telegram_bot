import logging

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery


from keyboards.inline.callback_datas import buy_mandarin_callback, rating_mandarin_callback
from keyboards.inline.inline_task_2 import products, menu
from loader import dp, bot

menu2 = menu


@dp.message_handler(Command('item'))
async def show_buy_mandarin(message: types.Message):
    for item in menu2:
        await bot.send_photo(message.from_user.id, menu2[item]['id'], 'продукт', reply_markup=products)
