from http import HTTPStatus

from fastapi.testclient import TestClient


def test_root(client: TestClient):
    """
    Triple A pattern
    A - Arrange - Arranjo
    A - Act - Executa a coisa
    A - Assert - Garanta que A e A
    """
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello, World!'}


def test_create_user(client: TestClient):
    response = client.post(
        '/users/',
        json={
            'id': 1,  # This field is not required in the request
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )
    print(response.status_code)
    assert response.status_code == HTTPStatus.CREATED
    print(response.json())
    assert response.json() == {
        'id': 1,
        'username': 'alice',
        'email': 'alice@example.com',
    }


def test_get_users(client: TestClient):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'alice',
                'email': 'alice@example.com',
            }
        ]
    }


def test_update_user(client: TestClient):
    response = client.put(
        '/users/1',
        json={
            'id': 1,
            'username': 'alice_updated',
            'email': 'alice@example.com',
            'password': 'new_secret',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'alice_updated',
        'id': 1,
        'email': 'alice@example.com',
    }


def test_delete_user(client: TestClient):
    response = client.delete('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted successfully'}
