from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile

from loader import dp, bot


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_file_id_p(message: types.Message):
    await message.reply(message.photo[-1].file_id)


@dp.message_handler(content_types=types.ContentType.VIDEO)
async def get_file_id_v(message: types.Message):
    await message.reply(message.video.file_id)


@dp.message_handler(Command("get_cat"))
async def send_cat(message: types.Message):
    # photo_file_id = '...'
    photo_url = 'https://i.ytimg.com/vi/1Ne1hqOXKKI/maxresdefault.jpg'
    # photo_bytes = InputFile(path_or_bytesio='photos/cat.jpg')
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=photo_url,
                         caption='This is cat\n'
                                 '/more_cats')
    await message.answer_video('BAACAgIAAxkBAAOpYhz-o7DUzMDlh4tvdFmGT1j0-lcAAtIWAAJMcehImgeHgphc-dojBA')


@dp.message_handler(Command("more_cats"))
async def more_cats(message: types.Message):
    album = types.MediaGroup()
    photo_file_id = 'AgACAgQAAxkBAAOhYhz4UEoalpp-wdMo64CLwJexlYEAAr2sMRt-aXxSYYjElvTozOABAAMCAAN3AAMjBA'
    video_file_id = 'BAACAgIAAxkBAAOpYhz-o7DUzMDlh4tvdFmGT1j0-lcAAtIWAAJMcehImgeHgphc-dojBA'
    photo_url = 'https://i.ytimg.com/vi/1Ne1hqOXKKI/maxresdefault.jpg'
    photo_bytes = InputFile(path_or_bytesio='photos/file_3.jpg')

    album.attach_photo(photo_file_id)
    album.attach_photo(photo_url)
    album.attach_photo(photo_bytes)
    album.attach_video(video_file_id,
                       caption='this is video')

    # await bot.send_media_group(chat_id=message.from_user.id, media=album)
    await message.answer_media_group(media=album)
