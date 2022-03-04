from typing import Union

import asyncpg
from asyncpg import pool, Connection

from data import config


class Database:
    def __init__(self):
        self.pool: Union[pool, None] = None

    async def create_pool(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME
        )

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                if fetchval:
                    result = await connection.fetchval(command, *args)
                if fetchrow:
                    result = await connection.fetchrow(command, *args)
                if execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(128) NOT NULL,
        username VARCHAR(128) NULL,
        telegram_id BIGINT NOT NULL
        );
        """
        await self.execute(sql, execute=True)

    async def create_user(self, full_name, username, telegram_id):
        sql = 'INSERT INTO users (full_name, username, telegram_id) VALUES($1, $2, $3) returning *'
        return await self.execute(sql, full_name, username, telegram_id, fetchrow=True)

    @staticmethod
    def format_kwargs(sql, parameters: dict):
        sql += ' AND '.join([
            f'{item} = ${num}' for num, item in enumerate(parameters.keys(), start=1)
        ])

        return sql, tuple(parameters.values())

    async def select_all_users(self):
        sql = 'SELECT * FROM users'
        return await self.execute(sql, fetch=True)

    async def select_user(self, **kwargs):
        sql = 'SELECT * FROM users WHERE '
        sql, parameters = self.format_kwargs(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def count_user(self):
        return await self.execute('SELECT COUNT(*) FROM users', fetchval=True)

    async def update_username(self, username, telegram_id):
        sql = 'UPDATE users SET username=$1 WHERE telegram_id=$2'
        return await self.execute(sql, username, telegram_id, execute=True)

    async def delete_all_users(self):
        sql = 'DELETE FROM users WHERE TRUE'
        await self.execute(sql, execute=True)

    async def delete_user(self, telegram_id):
        sql = "DELETE FROM users WHERE telegram_id=$1"
        await self.execute(sql, telegram_id, execute=True)
