import json

import pytest

import bytes_backend


@pytest.fixture()
def client():
    with bytes_backend.app.test_client() as client:
        yield client


@pytest.fixture()
def client_get(client):
    def _client_get(url, load_as_json=True):
        res = client.get(url).data
        return json.loads(res) if load_as_json else res
    return _client_get


def test_pong(client_get):
    assert client_get('/ping') == 'pong'
