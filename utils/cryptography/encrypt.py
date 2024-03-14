from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
import base64
from os.path import dirname

path = dirname(__file__)

with open(path+"/public_key_pem.pem", "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )


def encrypt(message: str):
    message = message.encode('utf-8')
    ciphertext = public_key.encrypt(
        message,
        padding.PKCS1v15()
    )
    b64 = base64.b64encode(ciphertext)
    return b64.decode()
