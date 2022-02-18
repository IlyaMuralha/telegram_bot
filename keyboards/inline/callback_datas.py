from aiogram.utils.callback_data import CallbackData


buy_callback = CallbackData('buy', 'item_name', 'quantity')

edit_callback = CallbackData('edit', 'item_name')

buy_mandarin_callback = CallbackData('buy', 'id')
rating_mandarin_callback = CallbackData('id', 'rating')
