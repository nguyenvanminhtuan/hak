import redis


class RedisStore:
    def __init__(self, url: str):
        self._store = redis.from_url(url)
