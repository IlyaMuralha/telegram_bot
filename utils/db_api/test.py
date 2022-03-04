import asyncio

from data import config
from utils.db_api import quick_commands
from utils.db_api.gino_db import db


async def test():
    await db.set_bind(config.POSTGRES_URI)
    await db.gino.drop_all()
    await db.gino.create_all()

    print('Add users')
    await quick_commands.add_user(1, 'one', '1@example.ru')
    await quick_commands.add_user(2, 'two', '2@example.ru')
    await quick_commands.add_user(3, 'three', '3@example.ru')
    await quick_commands.add_user(4, 'four', '4@example.ru')
    print('Done')

    users = list(map(str, await quick_commands.select_all_users()))
    print(f'All users: {users}')

    count = await quick_commands.count_users()
    print(f'Count users: {count}')

    user = await quick_commands.select_user(1)
    print(f'User: {user}')


loop = asyncio.get_event_loop()
loop.run_until_complete(test())
