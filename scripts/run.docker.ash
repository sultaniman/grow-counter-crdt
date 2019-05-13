#!/bin/ash

# wait a bit to make sure redis is up
sleep 2
pipenv run python app.py
