from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import menu
from loader import dp


@dp.message_handler(Command('menu'))
async def show_menu(message: types.Message):
    await message.answer('Push the button', reply_markup=menu)


# 1 вариант взаимодействия
@dp.message_handler(text='FirstLine')
async def first_line_button(message: types.Message):
    await message.answer('You push first line button')


# # 2 вариант взаимодействия
# @dp.message_handler(Text(equals=['SecondLineFirst', 'SecondLineSecond']))
# async def second_line_buttons(message: types.Message):
#     await message.answer(f'You push button: {message.text}')


# 3 вариант взаимодействия
@dp.message_handler(Text(startswith='SecondLine'))
async def second_line_buttons(message: types.Message):
    await message.answer(f'You push button: {message.text}', reply_markup=ReplyKeyboardRemove())
