import time
import os
import redis
from flask import Flask

app = Flask(__name__)
service=os.environ.get('SERVICE_DISCOVERY')
cache = redis.Redis(host=service, port=6379)


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
