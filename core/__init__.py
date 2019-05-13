import time

from typing import Dict
from starlette.applications import Starlette
from core import grow_counter, transport


app = Starlette(debug=True)

# Send updates every 2 seconds
UPDATE_INTERVAL = 2


class ViewCounter:
    def __init__(self):
        self.last_update = time.time()
        self.state = grow_counter.new()

    def increment(self):
        self.state = grow_counter.increment(self.state)

    def merge(self, updates: Dict):
        self.state = grow_counter.merge(self.state, updates)

    def reset_time(self):
        self.last_update = time.time()

    @property
    def count(self) -> int:
        return grow_counter.value(self.state)


def may_be_update(view_counter: ViewCounter):
    if time.time() - view_counter.last_update > UPDATE_INTERVAL:
        view_counter.reset_time()
        transport.send_updates(view_counter.state)
