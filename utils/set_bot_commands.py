from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Вывести справку"),
            types.BotCommand("set_photo", "Установить фото в чате"),
            types.BotCommand("set_title", "Установить название группе"),
            types.BotCommand("set_description", "Установить описание группе"),
            types.BotCommand("ro", "Режим Read Only"),
            types.BotCommand("unro", "Отменить RO"),
            types.BotCommand("ban", "Забанить"),
            types.BotCommand("unban", "Разбанить"),
        ]
    )
