import logging

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import buy_callback
from keyboards.inline.choise_buttons import choise, buy_pear_keyboard, buy_apple_keyboard
from loader import dp, bot


@dp.message_handler(Command('items'))
async def show_inline(message: types.Message):
    await message.answer('We have two products for you \n'
                         'apples and pears \n'
                         'If you do not need this push cancel.',
                         reply_markup=choise)


@dp.callback_query_handler(buy_callback.filter(item_name='pear'))
async def buying_pears(call: CallbackQuery, callback_data: dict):
    # закрываем часики
    # await bot.answer_callback_query(callback_query_id=call.id)
    await call.answer(cache_time=60)
    logging.info(f'CallbackData: {call.data}')
    logging.info(f'CallbackDataDict: {callback_data}')
    quantity = callback_data.get('quantity')
    await call.message.answer(f'You choose pears. Quantity: {quantity}. Thank you.',
                              reply_markup=buy_pear_keyboard)


@dp.callback_query_handler(buy_callback.filter(item_name='apple'))
async def buying_apples(call: CallbackQuery, callback_data: dict):
    # закрываем часики
    # await bot.answer_callback_query(callback_query_id=call.id)
    await call.answer(cache_time=60)
    logging.info(f'CallbackData: {call.data}')
    logging.info(f'CallbackDataDict: {callback_data}')
    quantity = callback_data.get('quantity')
    await call.message.answer(f'You choose apples. Quantity: {quantity}. Thank you.',
                              reply_markup=buy_apple_keyboard)


@dp.callback_query_handler(text_contains='cancel')
async def buying_cancel(call: CallbackQuery):
    logging.info(f'CallbackData: {call.data}')

    await call.answer(f'Goodbye', show_alert=True)

    await call.message.edit_reply_markup(reply_markup=None)


