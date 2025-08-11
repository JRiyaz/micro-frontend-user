from uuid import UUID, uuid4

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


def get_unique_id(hex_fmt=False) -> str:
    unique_id = uuid4()
    if hex_fmt:
        return unique_id.hex
    return str(unique_id)
