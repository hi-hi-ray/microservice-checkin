from random import *
from models import User


def create_auth(user, passw):
    user_exists = User.get_or_none(username=user)
    if user_exists is not None:
        return "Username already exists."
    else:
        creation = User.create(username=user, password=passw, token=__generate_token())
        if creation.token is not None:
            return "Created User"
        else:
            return "Failed Creating User"


def do_auth(user, passw):
    user_db = User.get(User.username == user)
    if user_db is not None:
        if user_db.username == user and user_db.password == passw:
            return user_db.token
        else:
            return "Username or Password invalid."
    else:
        return "Username does not exist."


def check_token(token):
    token_db = User.get(User.token == token)
    if token_db is not None:
        if token_db.token == token:
            return 'OK.'
        else:
            return "DENIED."
    else:
        return "DENIED."


def __generate_token():
    token_list = []
    token = ""
    items = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e',
             'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(8):
        token_list.append(choice(items))

    for token_item in token_list:
        token += token_item

    return token
