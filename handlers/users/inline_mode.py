from aiogram import types

from data import config
from loader import dp


@dp.inline_handler(text="")
async def empty_query(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id='Unknown',
                title='What do you want?',
                input_message_content=types.InputTextMessageContent(
                    message_text="Don't push the button!",
                    parse_mode='HTML'
                )
            )
        ], cache_time=5
    )


@dp.inline_handler()
async def some_query(query: types.InlineQuery):
    user = query.from_user.id
    if user not in config.allowed_users:
        await query.answer(
            results=[],
            switch_pm_text='Bot is not allowed yet. Allowed Bot.',
            switch_pm_parameter='connect_user',
            cache_time=5
        )
        return

    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id='1',
                title='Go to menu!',
                input_message_content=types.InputTextMessageContent(
                    message_text="This is <b>some</b> menu",
                    parse_mode='HTML'
                ),
                url='https://core.telegram.org/bots/api/#inline-mode',
                thumb_url='https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Telegram_logo.svg/'
                          '2048px-Telegram_logo.svg.png',
                description='description_url'
            )
        ], cache_time=5
    )
