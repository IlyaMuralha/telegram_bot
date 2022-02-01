from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states import UserForm


@dp.message_handler(Command('form'))
async def enter_name(message: types.Message):
    await message.answer('Начинаем заполнение формы: \n'
                         'Вопрос №1\n\n'
                         'Введи свое Имя')

    await UserForm.name.set()


@dp.message_handler(state=UserForm.name)
async def enter_email(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(name=answer)

    await message.answer('Вопрос №2\n\n'
                         'Введи свою почту')

    await UserForm.next()


@dp.message_handler(state=UserForm.email)
async def enter_phone(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(email=answer)

    await message.answer('Вопрос №3\n\n'
                         'Введи свой номер телефона')

    await UserForm.next()


@dp.message_handler(state=UserForm.phone)
async def final_form(message: types.Message, state: FSMContext):

    data = await state.get_data()
    name = data.get('name')
    email = data.get('email')
    phone = message.text

    await message.answer('Привет! Ты ввел следующие данные:\n\n'
                         f'Имя - {name} \n\n'
                         f'Email - {email}\n\n'
                         f'Телефон: - {phone}')

    await state.finish()
