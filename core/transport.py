import json
import redis

from functools import partial
from typing import Callable, Dict


connection = redis.StrictRedis()
channel = 'view-count'


def _listen(conn: redis.StrictRedis, merge_state: Callable):
    sub = conn.pubsub()
    sub.subscribe([channel])

    for event in sub.listen():
        try:
            merge_state(json.loads(event['data']))
        except (TypeError, ValueError):
            pass


def _send_updates(conn: redis.StrictRedis, updates: Dict):
    conn.publish(channel, json.dumps(updates))


listen = partial(_listen, connection)
send_updates = partial(_send_updates, connection)
