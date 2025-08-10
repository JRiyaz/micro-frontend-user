from uuid import UUID

from pydantic import EmailStr, ValidationError


def to_upper(value: str) -> str:
    return value.upper()


def is_valid_uuid(value: str) -> bool:
    try:
        uuid_obj = UUID(value)
        return str(uuid_obj) == value  # Ensure it's in correct format
    except ValueError:
        return False


def is_valid_email(value: str) -> bool:
    try:
        EmailStr._validate(value)
    except ValidationError:
        return False
    return True
