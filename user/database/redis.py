from redis.asyncio import Redis

from ..config import config


class RedisStorage:
    def __init__(self):
        self.redis_host = config.REDIS_HOST
        self.redis_port = config.REDIS_PORT
        self.redis_username = config.REDIS_USERNAME
        self.redis_password = config.REDIS_PASSWORD
        self.redis_db = config.REDIS_DB

        self.redis = Redis(host=self.redis_host, port=self.redis_port, db=self.redis_db, password=self.redis_password)

    async def set(self, key, value, ex=None):
        await self.redis.set(key, value, ex)

    async def get(self, key):
        return await self.redis.get(key)

    async def delete(self, key):
        await self.redis.delete(key)

    async def exists(self, key):
        return await self.redis.exists(key)

    async def set_expire(self, key, expire):
        await self.redis.expire(key, expire)

    async def close(self):
        await self.redis.close()
        await self.redis.connection_pool.disconnect()
