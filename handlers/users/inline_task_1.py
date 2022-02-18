import logging

from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.inline.edit_info_keyboard import edit_info
from loader import dp


@dp.message_handler(Command('inline_buttons_1'))
async def show_inline(message: types.Message):
    await message.answer('Edit @Sberleadbot info. \n\n'
                         'Name: Бот для Заданий на Курсе Udemy \n'
                         'Description: ? \n'
                         'About: ? \n'
                         'Botpic: ? no botpic \n'
                         'Commands: no commands yet',
                         reply_markup=edit_info)
