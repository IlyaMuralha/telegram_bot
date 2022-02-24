# "ro", "unro", "ban", "unban"
import asyncio
import datetime
import re

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.utils.exceptions import BadRequest

from filters import IsGroup, AdminFilter
from loader import dp, bot


@dp.message_handler(IsGroup(), Command('ro', prefixes="!/"), AdminFilter())
async def read_only_mode(message: types.Message):
    """
    устанавливает режим "только чтения" для пользователя
    """
    # получаем id пользователя
    member = message.reply_to_message.from_user
    member_id = member.id
    # получаем id чата
    chat_id = message.chat.id
    # парсим команду считывая на сколько поставить режим "только чтение"
    parse_command = re.compile(r"(!ro|/ro) ?(\d+)? ?([\w+\D]+)?")
    parsed = parse_command.match(message.text)
    time_ro = parsed.group(2)
    comment = parsed.group(3)
    if not time_ro:
        time_ro = 5
    else:
        time_ro = int(time_ro)
    # получаем конкретное время до какого баним
    until_date = datetime.datetime.now() + datetime.timedelta(minutes=time_ro)

    # сформировываем что конкретно запрещаем
    ReadOnlyPermissions = types.ChatPermissions(
        can_send_messages=False,
        can_send_media_messages=False,
        can_pin_messages=False,
        can_send_polls=False,
        can_change_info=False,
        can_send_other_messages=False,
        can_invite_users=True,
        can_add_web_page_previews=False
    )
    try:
        # данный метод доступен только для супергрупп
        await bot.restrict_chat_member(chat_id,
                                       user_id=member_id,
                                       permissions=ReadOnlyPermissions,
                                       until_date=until_date)
        await message.reply(f'Пользователю {member.get_mention(as_html=True)} запрещено писать на '
                            f'{time_ro} минут. По причине {comment}.')
    except BadRequest:
        await message.answer('Пользователь администратор')

    service_message = await message.reply("Сообщение самоуничтожится через 5 сек")
    await asyncio.sleep(5)
    await message.delete()
    await service_message.delete()


@dp.message_handler(IsGroup(), Command('unro', prefixes="!/"), AdminFilter())
async def not_read_only_mode(message: types.Message):
    """
    убирает режим "только чтения" для пользователя
    """
    # получаем id пользователя
    member = message.reply_to_message.from_user
    member_id = member.id

    user_allowed = types.ChatPermissions(
        can_send_messages=True,
        can_send_media_messages=True,
        can_pin_messages=False,
        can_send_polls=True,
        can_change_info=False,
        can_send_other_messages=True,
        can_invite_users=True,
        can_add_web_page_previews=True
    )

    await message.chat.restrict(user_id=member_id, permissions=user_allowed, until_date=0)
    await message.reply(f'Пользователь {member.get_mention(as_html=True)} разбанен')


@dp.message_handler(IsGroup(), Command('ban', prefixes="!/"), AdminFilter())
async def ban_mode(message: types.Message):
    """
    обработчик банит указанного пользователя
    """
    # получаем id пользователя
    member = message.reply_to_message.from_user
    member_id = member.id
    # получаем id чата
    chat_id = message.chat.id

    await message.chat.kick(user_id=member_id)
    await message.reply(f'Пользователь {member.get_mention(as_html=True)} забанен')


@dp.message_handler(IsGroup(), Command('unban', prefixes="!/"), AdminFilter())
async def unban_mode(message: types.Message):
    """
    обработчик разбанит указанного пользователя
    """
    # получаем id пользователя
    member = message.reply_to_message.from_user
    member_id = member.id

    await message.chat.unban(user_id=member_id)
    await message.reply(f'Пользователь {member.get_mention(as_html=True)} разбанен')

