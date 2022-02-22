import io

from aiogram import types
from aiogram.dispatcher.filters import Command

from filters import IsGroup
from filters.admins import AdminFilter
from loader import dp, bot


# устанавливаем префиксы для обозначения начала команды
# устанавливаем админ-фильтр, который срабатывает только
# при обращении к команде 'set_photo'
@dp.message_handler(IsGroup(), Command('set_photo', prefixes="!/"), AdminFilter())
async def set_new_photo(message: types.Message):
    """
    устанавливает новое фото чата
    """
    # обращаемся
    source_message = message.reply_to_message
    # вытаскиваем фото из объекта сообщения
    photo = source_message.photo[-1]
    # сохраняем фото в байтах
    photo = await photo.download(destination=io.BytesIO())
    # подгружаем только что сохраненное фото из памяти
    input_file = types.InputFile(photo)
    # устанавливаем фото чата
    # await bot.set_chat_photo(chat_id=message.chat.id, photo=input_file)
    await message.chat.set_photo(photo=input_file)
    await source_message.delete()


@dp.message_handler(IsGroup(), Command('set_title', prefixes="!/"), AdminFilter())
async def set_new_title(message: types.Message):
    """
    устанавливает новое название чата
    """
    source_message = message.reply_to_message
    title = source_message.text
    await message.chat.set_title(title=title)
    await source_message.delete()


@dp.message_handler(IsGroup(), Command('set_description', prefixes="!/"), AdminFilter())
async def set_new_description(message: types.Message):
    """
    устанавливает новое название чата
    """
    source_message = message.reply_to_message
    description = source_message.text
    await message.chat.set_description(description=description)
    await source_message.delete()

