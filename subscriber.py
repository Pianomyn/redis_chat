import redis

r = redis.Redis()
subscriber = r.pubsub()
subscriber.subscribe("chat")

for message in subscriber.listen():
    if message["data"] and type(message["data"]) is bytes:
        decoded_msg = message["data"].decode("utf-8")
        #yield decoded_msg
        print(decoded_msg)
