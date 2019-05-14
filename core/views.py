import time

from starlette.responses import JSONResponse
from core import app, grow_counter, may_be_update, ViewCounter


view_counter = ViewCounter()


@app.route('/my-video')
async def homepage(_request):
    view_counter.increment()

    return JSONResponse({
        'view_count': grow_counter.value(view_counter.state)
    })


def merge_state(updates):
    view_counter.merge(updates)


def sync():
    while True:
        time.sleep(1)
        may_be_update(view_counter)
