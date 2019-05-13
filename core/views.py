from starlette.responses import JSONResponse
from core import app, grow_counter, may_be_update, ViewCounter


view_counter = ViewCounter()


def merge_state(updates):
    view_counter.merge(updates)


@app.route('/')
async def homepage(_request):
    view_counter.increment()
    may_be_update(view_counter)

    return JSONResponse({
        'view_count': grow_counter.value(view_counter.state)
    })