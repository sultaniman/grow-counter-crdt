FROM python:3.7.3-alpine3.9

WORKDIR /app
COPY . /app

RUN apk update && \
    apk add --update netcat-openbsd && \
    apk add --no-cache --virtual .build-deps build-base && \
    pip install pip pipenv -U && \
    pipenv install && \
    apk del .build-deps  && \
    rm -rf /root/.cache/pip

EXPOSE 8000

CMD ["scripts/run.docker.ash"]
