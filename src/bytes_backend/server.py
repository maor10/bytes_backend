from flask import Flask

from src.bytes_backend.decorators import bytes_response
from src.bytes_backend.orm.db import connect_to_db

app = Flask(__name__)


@app.route('/ping')
@bytes_response()
def pong():
    return "pong"


if __name__ == '__main__':
    connect_to_db()
    app.run('0.0.0.0', debug=True)
