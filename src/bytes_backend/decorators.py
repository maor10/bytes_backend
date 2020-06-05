import json
from functools import wraps


def bytes_response(dump_as_json=True):

    def _decorator(f):

        @wraps(f)
        def _wrapper(*args, **kwargs):
            try:
                res = f(*args, **kwargs)
                return json.dumps(res) if dump_as_json else res
            except Exception as e:
                return json.dumps({
                    'failed': f'General Exception: {e}'
                })

        return _wrapper

    return _decorator
