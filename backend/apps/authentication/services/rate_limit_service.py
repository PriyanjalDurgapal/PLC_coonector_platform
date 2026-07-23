from redis.exceptions import RedisError

from .redis_service import RedisService


class RateLimitService:
    MAX_ATTEMPTS = 2
    BLOCK_TIME = 1 * 60  # 15 minutes (seconds)

    @classmethod
    def _key(cls, username, ip):
        return f"login_attempt:{username}:{ip}"

    @classmethod
    def is_blocked(cls, username, ip):
        """
        Returns True if the user has exceeded the maximum
        number of failed login attempts.

        If Redis is unavailable, do not block the login.
        """
        try:
            client = RedisService.get_client()

            attempts = client.get(cls._key(username, ip))

            if attempts is None:
                return False

            return int(attempts) >= cls.MAX_ATTEMPTS

        except RedisError:
            return False

    @classmethod
    def record_failed_attempt(cls, username, ip):
        """
        Increments the failed login attempt counter.

        The expiry is only set when the key is created
        so the block duration stays fixed.
        """
        try:
            client = RedisService.get_client()

            key = cls._key(username, ip)

            attempts = client.incr(key)

            if attempts == 1:
                client.expire(key, cls.BLOCK_TIME)

        except RedisError:
            # Ignore Redis errors so login continues normally.
            pass

    @classmethod
    def reset_attempts(cls, username, ip):
        """
        Clears failed login attempts after a successful login.
        """
        try:
            client = RedisService.get_client()

            client.delete(cls._key(username, ip))

        except RedisError:
            # Ignore Redis errors.
            pass