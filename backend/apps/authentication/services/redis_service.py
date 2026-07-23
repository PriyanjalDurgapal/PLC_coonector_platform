import redis
from django.conf import settings


class RedisService:
    _client = redis.Redis(
        host=getattr(settings, "REDIS_HOST", "127.0.0.1"),
        port=getattr(settings, "REDIS_PORT", 6379),
        db=0,
        decode_responses=True,
    )

    @classmethod
    def get_client(cls):
        return cls._client