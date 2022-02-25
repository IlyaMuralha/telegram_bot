from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


check_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Проверить подписки',
                                 callback_data="check_subs")
        ]
    ]
)
