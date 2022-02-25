from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Вывести справку"),
            types.BotCommand("channels", "список каналов на подписку"),
            types.BotCommand("create_post", "предложить пост в канале"),
        ]
    )
