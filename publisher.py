import redis

r = redis.Redis()

while True:
    username = input("Please enter your username: ")
    if not r.sismember("usernames", username):
        r.sadd("usernames", username)
        break
    else:
        print("This username is already taken!")

while True:
    val = input("Please enter your message: ")
    r.publish("chat", "{}: {}".format(username, val))
