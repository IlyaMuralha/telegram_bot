from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import buy_mandarin_callback, rating_mandarin_callback

APPLE_LINK = 'https://klike.net/uploads/posts/2019-06/1561279259_1.jpg'

PEAR_LINK = 'https://delikates.ua/images/product/grusha.jpg'

menu = {
    'apple': {'id': 1, 'photo': APPLE_LINK},
    'pear': {'id': 2, 'photo': PEAR_LINK}
}

products = InlineKeyboardMarkup()
for item in menu:
    products.add(InlineKeyboardButton(text="Купить продукт",
                                      callback_data=buy_mandarin_callback.new(id=menu[item]['id'])))


