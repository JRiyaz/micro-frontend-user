from cryptography.fernet import Fernet

from ..model.user import User

SECRET_KEY: bytes = b"_jG6o61sMUw-dRgnNViSv-B5K86AP9f7GjxwghhJ9Ew="  # Fernet.generate_key()

DEFAULT_USERS = [
    {
        "username": "riyaz",
        "email": "riyaz@example.com",
        "firstName": "Riyaz",
        "lastName": "Khan",
        "id": "819486b8-81d4-462f-a9fd-9eb026c93c4c",
        "password": f"{Fernet(SECRET_KEY).encrypt(b'pass').decode('utf8')}",
    },
    {
        "username": "fayaz",
        "email": "fayaz@example.com",
        "firstName": "Fayaz",
        "lastName": "Khan",
        "id": "176a9d43-6dc2-411b-aaa4-bf2158640461",
    },
    {
        "username": "azu",
        "email": "azu@example.com",
        "firstName": "Azu",
        "lastName": "Azu",
        "id": "fed04edc-4c84-4923-b1a1-038ed4bbb068",
    },
    {
        "username": "khan",
        "email": "Khan@example.com",
        "firstName": "Khan",
        "lastName": "Riyaz",
        "id": "fa6423a4-dbec-4c6a-b822-6621796ed278",
    },
]

USERS: list[User] = [User(**usr) for usr in DEFAULT_USERS]
