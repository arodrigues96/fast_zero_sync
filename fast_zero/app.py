from http import HTTPStatus

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message, UserDB, UserList, UserPublic, UserSchema

app = FastAPI()

database = []


@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {"message": "Hello World", "batata": "frita"}


@app.get("/exercicio2", status_code=HTTPStatus.OK, response_class=HTMLResponse)  # HTML RESPONSE - response_class muda a classe de JSON pra HTML
def exercicio2():
    return """
    <html>
        <head>
            <title> FastAPI do Deco </title>
        </head>
        <body>
            <h1> Meu teste de app </h1>
            <h2> Testando resposta HTML e PyTest de função :D </h2>
        </body>
    </html>"""


@app.post("/users/", status_code=HTTPStatus.CREATED, response_model=UserPublic)  # Referencia UserPublic pra não expor senha
def create_user(user: UserSchema):
    user_with_id = UserDB(id=len(database) + 1, **user.model_dump())

    database.append(user_with_id)

    return user_with_id


@app.get("/users/", response_model=UserList)
def read_user():
    return {"users": database}

@app.get("/users/{user_id}") #Exercicio
def read_specific_user(user_id: int):
    user = database[user_id - 1]
    return user


@app.put("/users/{user_id}", response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    if user_id < 1 or user_id > len(database) + 1:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="User not found!")
    user_with_id = UserDB(**user.model_dump(), id=user_id)
    database[user_id - 1] = user_with_id

    return user_with_id


@app.delete("/users/{user_id}", response_model=Message)
def delete_user(user_id: int):
    if user_id < 1 or user_id > len(database) + 1:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="User not found!")
    del database[user_id - 1]
    return {"message": "User deleted!"}
