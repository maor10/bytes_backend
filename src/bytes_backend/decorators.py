import json
import os
from functools import wraps

from bson import ObjectId
from flask import session

from bytes_backend.orm.user import User


def get_or_create_user() -> User:
    if 'user_id' in session:
        return User.objects.get(id=ObjectId(session['user_id']))
    user = User(anonymous=True).save()
    session['user_id'] = str(user.id)
    return user


def bytes_response(dump_as_json=True, load_user=True):

    def _decorator(f):

        @wraps(f)
        def _wrapper(*args, **kwargs):
            try:
                if load_user:
                    user = get_or_create_user()
                    kwargs['user'] = user
                res = f(*args, **kwargs)
                return json.dumps(res) if dump_as_json else res
            except Exception as e:
                debug = os.environ.get('DEBUG', True)
                message = f'General Exception: {e}' if debug else 'Server Error'
                return json.dumps({
                    'failed': message
                })

        return _wrapper

    return _decorator
