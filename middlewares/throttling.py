import asyncio
from typing import Union

from aiogram import types, Dispatcher
from aiogram.dispatcher import DEFAULT_RATE_LIMIT
from aiogram.dispatcher.handler import CancelHandler, current_handler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.utils.exceptions import Throttled


# class ThrottlingMiddleware(BaseMiddleware):
#     """
#     Simple middleware
#     """
#
#     def __init__(self, limit=DEFAULT_RATE_LIMIT, key_prefix='antiflood_'):
#         self.rate_limit = limit
#         self.prefix = key_prefix
#         super(ThrottlingMiddleware, self).__init__()
#
#     async def on_process_message(self, message: types.Message, data: dict):
#         handler = current_handler.get()
#         dispatcher = Dispatcher.get_current()
#         if handler:
#             limit = getattr(handler, "throttling_rate_limit", self.rate_limit)
#             key = getattr(handler, "throttling_key", f"{self.prefix}_{handler.__name__}")
#         else:
#             limit = self.rate_limit
#             key = f"{self.prefix}_message"
#         try:
#             await dispatcher.throttle(key, rate=limit)
#         except Throttled as t:
#             await self.message_throttled(message, t)
#             raise CancelHandler()
#
#     async def message_throttled(self, message: types.Message, throttled: Throttled):
#         if throttled.exceeded_count <= 2:
#             await message.reply("Too many requests!")


class ThrottlingMiddleware(BaseMiddleware):

    def __init__(self, limit=DEFAULT_RATE_LIMIT, key_prefix='antiflood_'):
        self.limit = limit
        self.prefix = key_prefix
        super(ThrottlingMiddleware, self).__init__()

    async def throttle(self, target: Union[types.Message, types.CallbackQuery]):
        handler = current_handler.get()
        if not handler:
            return

        dp = Dispatcher.get_current()
        limit = getattr(handler, 'throttling_rate_limit', self.limit)
        key = getattr(handler, 'throttling_key', f'{self.prefix}_{handler.__name__}')

        try:
            await dp.throttle(key, rate=limit)
        except Throttled as t:
            await self.target_throttled(target, t, dp, key)
            raise CancelHandler

    @staticmethod
    async def target_throttled(target: Union[types.Message, types.CallbackQuery],
                               throttled: Throttled, dispatcher: Dispatcher, key: str):
        msg = target.message if isinstance(target, types.CallbackQuery) else target

        delta = throttled.rate - throttled.delta
        if throttled.exceeded_count == 2:
            await msg.reply('?????????????? ?????????? ??????????????????!)')
            return
        elif throttled.exceeded_count == 3:
            await msg.reply(f'??????. ???????????? ???? ???????????? ???????? ???? ?????????????? {int(delta)} ????????????!)')
            return
        await asyncio.sleep(delta)

        thr = await dispatcher.check_key(key)
        if thr.exceeded_count == throttled.exceeded_count:
            await msg.reply('??????, ???????????? ??????????????!)')

    async def on_process_message(self, message, data):
        await self.throttle(message)

    async def on_process_callback_query(self, call, data):
        await self.throttle(call)
