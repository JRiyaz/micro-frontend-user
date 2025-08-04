from pydantic import BaseModel


class DetailMessage(BaseModel):
    detail: str


class Message(BaseModel):
    msg: str
