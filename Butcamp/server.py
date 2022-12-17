import redis
import random

with redis.Redis() as redis_server:
    redis_server.lpush("que", random.randint(0, 10))
   


