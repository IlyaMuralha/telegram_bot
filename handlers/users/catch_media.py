from aiogram import types

from loader import dp


@dp.message_handler()
async def catch_text(message: types.Message):
    await message.answer('Вы прислали текстовое сообщение')


@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def catch_doc(message: types.Message):
    await message.document.download()
    await message.reply(f'Документ был успешно скачан \n'
                        f'<pre>FILE_ID = {message.document.file_id}</pre>',
                        parse_mode='HTML')


@dp.message_handler(content_types=types.ContentType.AUDIO)
async def catch_audio(message: types.Message):
    await message.audio.download()
    await message.reply(f'Аудио было успешно скачано \n'
                        f'<pre>FILE_ID = {message.audio.file_id}</pre>',
                        parse_mode='HTML')


@dp.message_handler(content_types=types.ContentType.VIDEO)
async def catch_video(message: types.Message):
    await message.video.download()
    await message.reply(f'Видео было успешно скачано \n'
                        f'<pre>FILE_ID = {message.video.file_id}</pre>',
                        parse_mode='HTML')


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def catch_photo(message: types.Message):
    await message.photo[-1].download()
    await message.reply(f'Фото было успешно скачано \n'
                        f'<pre>FILE_ID = {message.photo[-1].file_id}</pre>',
                        parse_mode='HTML')


@dp.message_handler(content_types=types.ContentType.ANY)
async def catch_any(message: types.Message):
    await message.reply(f'Вы прислали: {message.content_type}')
