from ..model.user import User

DEFAULT_USERS = [
    {
        "username": "riyaz",
        "email": "riyaz@example.com",
        "firstName": "Riyaz",
        "lastName": "Khan",
        "id": "819486b8-81d4-462f-a9fd-9eb026c93c4c",
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
