from cryptography.fernet import Fernet, InvalidToken

from ..utils.constants import SECRET_KEY

FERNET: Fernet = Fernet(SECRET_KEY)


def encrypt_password(password: str) -> str:
    return FERNET.encrypt(password.encode("utf-8")).decode("utf-8")


def decrypt_password(password: str) -> str:
    return FERNET.decrypt(password.encode("utf-8")).decode("utf-8")


def is_encrypted(password: str) -> bool:
    try:
        # Try to decrypt with your `FERNET` instance
        FERNET.decrypt(password.encode("utf-8"))
        return True  # It was successfully decrypted, so it was encrypted
    except InvalidToken:
        # If an InvalidToken exception occurs, it's not a valid encrypted string
        return False
