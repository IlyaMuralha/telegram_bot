from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsForwarded(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        if message.forward_from_chat:
            # дополнительно проверяем, что это не просто пересланное сообщение,
            # а оно пересланно из канала
            return message.forward_from_chat.type == types.ChatType.CHANNEL
