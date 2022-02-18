from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import edit_callback

edit_info = InlineKeyboardMarkup(row_width=2,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(
                                             text='Edit Name',
                                             callback_data=edit_callback.new(item_name='name')
                                         ),
                                         InlineKeyboardButton(
                                             text='Edit Description',
                                             callback_data=edit_callback.new(item_name='description')
                                         ),
                                     ],
                                     [
                                         InlineKeyboardButton(
                                             text='Edit About',
                                             callback_data=edit_callback.new(item_name='about')
                                         ),
                                         InlineKeyboardButton(
                                             text='Edit Botpic',
                                             callback_data=edit_callback.new(item_name='botpic')
                                         ),
                                     ],
                                     [
                                         InlineKeyboardButton(
                                             text='Edit Commands',
                                             callback_data=edit_callback.new(item_name='commands')
                                         ),
                                         InlineKeyboardButton(
                                             text='<<Back to Bot',
                                             callback_data=edit_callback.new(item_name='cancel')
                                         ),
                                     ],
                                 ]
                                 )
