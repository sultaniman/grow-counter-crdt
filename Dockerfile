FROM python:3.7.3-alpine3.9

WORKDIR /app
COPY . /app

RUN pip install pip pipenv -U &&\
    pipenv install

ENTRYPOINT ["pipenv", "run", "python app.py"]
