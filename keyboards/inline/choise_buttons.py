from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import buy_callback

choise = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text="Let's buy a pear",
                                          # callback_data='pear'
                                          callback_data=buy_callback.new(item_name='pear',
                                                                         quantity=1)
                                      ),
                                      InlineKeyboardButton(
                                          text="Let's buy an apple",
                                          callback_data='buy:apple:5'
                                      ),
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text='Cancel',
                                          callback_data='cancel'
                                      )
                                  ]
                              ])

buy_pear_keyboard = InlineKeyboardMarkup()

PEAR_LINK = 'https://www.google.com/search?q=%D0%B3%D1%80%D1%83%D1%88%D0%B0&sxsrf=APq-WBuQNrnPDaxQWL2YZbG-ygdZasHUbg:1643785506109&source=lnms&tbm=isch&sa=X&ved=2ahUKEwikpLaZuuD1AhXmmIsKHUqOAFIQ_AUoAXoECAIQAw&biw=1536&bih=722&dpr=1.25'
pear_link = InlineKeyboardButton(text='Buy here', url=PEAR_LINK)

buy_pear_keyboard.insert(pear_link)


buy_apple_keyboard = InlineKeyboardMarkup()

APPLE_LINK = 'https://www.google.com/search?q=%D1%8F%D0%B1%D0%BB%D0%BE%D0%BA%D0%BE&tbm=isch&ved=2ahUKEwj9qd-auuD1AhV1lFwKHS7UDNYQ2-cCegQIABAA&oq=z%2Ckjrj&gs_lcp=CgNpbWcQARgAMgQIABBDMgQIABBDMgQIABAKMgQIABAKMgQIABAKMgQIABAKMgQIABAKMgQIABBDMgQIABAKMgQIABAKOgcIIxDvAxAnOgUIABCABDoICAAQgAQQsQM6CQgAEIAEEAoQAToECAAQHlCnF1i5NGCTQmgAcAB4AIABcogBwQWSAQM0LjOYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=JC36Yf2HNfWo8gKuqLOwDQ&bih=722&biw=1536'
apple_link = InlineKeyboardButton(text='Buy here', url=APPLE_LINK)

buy_apple_keyboard.insert(apple_link)
