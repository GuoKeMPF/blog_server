from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import base64

from os.path import dirname

path = dirname(__file__)

with open(path+"/private_key_pem.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )


def decrypt(b64):
    message = b64.encode('utf-8')
    encrypted = base64.b64decode(message)
    result = private_key.decrypt(
        encrypted,
        padding.PKCS1v15()
    )
    result = result.decode('utf-8')
    return result
