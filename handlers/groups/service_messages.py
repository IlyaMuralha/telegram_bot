from aiogram import types

from loader import dp, bot


@dp.message_handler(content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def hello_new_member(message: types.Message):
    members = ', '.join([m.get_mention(as_html=True) for m in message.new_chat_members])
    # # если нужно приветствовать по одному
    # await message.reply(f'Привет, {message.new_chat_members[0].full_name}!')
    await message.reply(f'Привет, {members}!')


@dp.message_handler(content_types=types.ContentType.LEFT_CHAT_MEMBER)
async def bay_member(message: types.Message):
    """
    обработчик сообщений об удалении пользователя
    """
    if message.left_chat_member.id == message.from_user.id:
        await message.answer(f'Пользователь {message.left_chat_member.get_mention(as_html=True)} вышел из чата!')
    elif message.from_user.id == (await bot.me).id:
        return
    else:
        await message.answer(f'{message.left_chat_member.full_name} был удалён из чата '
                             f'пользователем {message.from_user.get_mention(as_html=True)}!')
