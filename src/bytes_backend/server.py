from bytes_backend.blueprints.courses.courses import courses_blueprint
from bytes_backend.blueprints.steps.steps import steps_blueprint
from bytes_backend.decorators import bytes_response
from bytes_backend.orm.db import connect_to_db
from flask import Flask


app = Flask(__name__)
app.secret_key = 'Nigga\'s like wiggas'

app.register_blueprint(courses_blueprint, url_prefix='/courses')
app.register_blueprint(steps_blueprint, url_prefix='/steps')


@app.route('/ping')
@bytes_response(load_user=False)
def pong():
    return "pong"


if __name__ == '__main__':
    connect_to_db()
    app.run('0.0.0.0', debug=True)
