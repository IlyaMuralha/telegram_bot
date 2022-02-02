from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='FirstLine')
        ],
        [
            KeyboardButton(text='SecondLineFirst'),
            KeyboardButton(text='SecondLineSecond'),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
