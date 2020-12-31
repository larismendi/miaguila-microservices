import os
import tempfile
import sqlite3

import pytest

from app import create_app
from flask import g
from flask_sqlalchemy import SQLAlchemy

# with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
#     _data_sql = f.read().decode('utf8')

def get_db(app):
    if 'db' not in g:
        g.db = SQLAlchemy(app)

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db(app):
    db = get_db(app)

    with app.open_resource('schema.sql') as f:
        db.engine.execute(f.read().decode('utf8'))

@pytest.fixture
def app():
    app = create_app('config.testing')

    with app.app_context():
        init_db(app)
    
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()