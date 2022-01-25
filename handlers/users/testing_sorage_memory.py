from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states import Test


@dp.message_handler(Command('test'))
async def enter_test(message: types.Message):
    await message.answer('Testing is start.\n'
                         'Question 1.\n\n'
                         'Are you ready? (Y/N)')


    # состояние может быть задано несколькими вариантами
    await Test.Q1.set()
    # await Test.first()


@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text

    # # сохраняем ответ пользователя в машине состояний одним из способов
    await state.update_data(answer1=answer)

    # await state.update_data({
    #     'answer1': answer,
    # })

    # async with state.proxy() as data:
    #     data['answer1'] = answer

    await message.answer('Question 2. \n\n'
                         'Are you still ready? (Y/N)')

    # переключаем на второе состояние
    await Test.next()
    # await Test.Q2


@dp.message_handler(state=Test.Q2)
async def answer_q2(message: types.Message, state: FSMContext):

    data = await state.get_data()
    answer1 = data.get('answer1')
    answer2 = message.text

    await message.answer('Thank you for your opinion.')
    await message.answer(f'Your answer 1: {answer1}')
    await message.answer(f'Your answer 2: {answer2}')

    # # сбрасываем состояние для пользователя
    await state.finish()
    # await state.reset_state()
    # # сбрасываем состояние, но данные оставляем
    # await state.reset_state(with_data=False)
