from aiogram import Dispatcher

from loader import dp
from .throttling import ThrottlingMiddleware
from .big_brother import BigBrotherMiddleware


if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(BigBrotherMiddleware())
