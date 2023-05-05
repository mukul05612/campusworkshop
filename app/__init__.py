"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaanu2k728r8871jlrg-a.oregon-postgres.render.com",
        database="todo_k0v3",
        user="root",
        password="m6nDDqw1XsniwCAN7kKKGhqebDcJmRHb")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
