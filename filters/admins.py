from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class AdminFilter(BoundFilter):
    """
    класс проверяет является ли пользователь от которого пришло сообщение
    администратором и возвращает bool
    """
    async def check(self, message: types.Message) -> bool:
        member = await message.chat.get_member(message.from_user.id)
        return member.is_chat_admin()