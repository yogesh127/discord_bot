import hashlib
import json

import redis

with open('config.json', 'r') as f:
    config = json.load(f)
r = redis.StrictRedis(host=config['redis']['host'], port=config['redis']['port'], password=config['redis']['password'],
                      decode_responses=True)

# redis cache is used for storing key and value
# we fetch value and append new value with it
# insert updated value for the key
def put_db(key, value):
    msg = r.get(key)
    if not msg:
        r.set(key, value)
        print(msg)
    else:
        msg = value + ' ' + msg
        r.set(key, msg)

# Redis Cache
# fetch the value from redis on the based of key
#
def get_db(key):
    msg = r.get(key)
    return msg
