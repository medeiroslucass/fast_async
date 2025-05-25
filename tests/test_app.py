from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_async.app import app

# Arrange
client = TestClient(app)


def test_root():
    """
    Triple A pattern
    A - Arrange - Arranjo
    A - Act - Executa a coisa
    A - Assert - Garanta que A e A
    """
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello, World!'}
