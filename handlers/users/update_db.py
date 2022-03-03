from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp, db


@dp.message_handler(Command('Email'))
async def ask_email(message: types.Message, state: FSMContext):
    await message.answer('Send me your email')
    await state.set_state('email')


@dp.message_handler(state='email')
async def get_email(message: types.Message, state: FSMContext):
    email = message.text
    db.update_email(email=email, id=message.from_user.id)
    user = db.select_user(id=message.from_user.id)
    await message.answer(f'Update data: {user}')
    await state.finish()
