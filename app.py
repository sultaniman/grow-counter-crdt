import uvicorn

from threading import Thread

from core import app, transport
from core.views import merge_state


if __name__ == '__main__':
    Thread(target=transport.listen, args=(merge_state,)).start()
    uvicorn.run(app, host='0.0.0.0', port=8000)
