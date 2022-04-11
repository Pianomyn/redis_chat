import redis

r = redis.Redis()

while True:
    val = input()
    r.publish("chat", val)
