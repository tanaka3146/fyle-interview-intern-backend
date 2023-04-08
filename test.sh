#!/bin/bash


set -e


export FLASK_APP=core/server.py

rm -rf core/store.sqlite3

flask db upgrade -d core/migrations/

pytest -vvv -s tests
