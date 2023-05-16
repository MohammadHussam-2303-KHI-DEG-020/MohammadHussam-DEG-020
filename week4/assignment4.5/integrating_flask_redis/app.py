import os
import time
import redis
from flask import Flask

app = Flask(__name__)
redis_host = os.environ.get('REDIS_HOST')
redis_port = int(os.environ.get('REDIS_PORT'))
print('My Redis host: ', redis_host)
print('My Redis post: ', redis_port)
try:
    cache = redis.Redis(host=redis_host, port=redis_port)
except Exception as e:
    print('Exception: My Redis host: ', redis_host)
    print('Exception: My Redis post: ', redis_port)


def get_and_increase_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr("hits")
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route("/")
def hello():
    count = get_and_increase_hit_count()
    return "Hello World! I have been seen {} times.\n".format(count)
