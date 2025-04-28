from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_ola_mundo(client):  # Nome descritivo
    response = client.get("/")  # Act (açãoo,executa algo)

    assert response.status_code == HTTPStatus.OK  # Assert (afirmar)
    assert response.json() == {"message": "Hello World"}


def test_exercicio_2_retornar_ok_e_html(client):
    response = client.get("/exercicio2")

    assert response.status_code == HTTPStatus.OK
    assert "<h1> Meu teste de app </h1>" in response.text


def test_create_user(client):
    response = client.post("/users/", json={"username": "test", "email": "test@example.com", "password": "testing"})
    # Validar Response Code
    assert response.status_code == HTTPStatus.CREATED
    # Validar UserPublic
    assert response.json() == {"username": "test", "email": "test@example.com", "id": 1}


def test_read_user(client):
    response = client.get("/users/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"users": [{"username": "test", "email": "test@example.com", "id": 1}]}


def test_update_user(client):
    response = client.put("/users/1", json={"username": "icarus", "email": "bk@example.com", "password": "test-pass"})

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"id": 1, "username": "icarus", "email": "bk@example.com"}


def test_update_error(client):
    response = client.put("/users/3", json={"username": "icarus", "email": "bk@example.com", "password": "test-pass"})

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user(client):
    response = client.delete("/users/1")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "User deleted!"}


def test_delete_error(client):
    response = client.delete("users/2")

    assert response.status_code == HTTPStatus.NOT_FOUND
