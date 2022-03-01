from io import BytesIO
from pathlib import Path

from aiogram import types

from loader import dp


@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def download_doc(message: types.Message):
    path_to_download = Path().joinpath('items', 'categories', 'photos')
    path_to_download.mkdir(parents=True, exist_ok=True)
    path_to_download = path_to_download.joinpath(message.document.file_name)

    await message.document.download(destination=path_to_download)
    await message.answer(f'We download document to {path_to_download}')


@dp.message_handler(content_types=types.ContentType.AUDIO)
async def get_audio(message: types.Message):
    if message.document:
        file_id = message.document.file_id
    elif message.audio:
        file_id = message.audio.file_id

    await message.answer(f'ID Audio == {file_id}')
    await message.answer_document(file_id)


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def convert_photo(message: types.Message):
    save_to_io = BytesIO()
    await message.photo[-1].download(destination=save_to_io)

    await message.answer_document(types.InputFile(save_to_io, filename='photo.jpg'))
