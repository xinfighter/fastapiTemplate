from passlib.context import CryptContext

crypt = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")
