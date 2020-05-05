# Nathan Park
# nyp5aa

import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

LIST_OF_FILES_TO_NOT_ENCRYPT_OR_DECRYPT = [
    "decrypt.py",
    "encrypt.py",
    "helpers.py",
    "password",
    "README.md"
]


def generate_sym_key():
    password_provided = open("password", "r").read().strip()
    password = password_provided.encode() # Convert to type bytes
    salt = b'W\xda\xb9\x16\xcb\xf4M:\x07\x81\xa5\xed\x80\xef\xdd\x88'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key


def get_files():
    paths_to_files = []
    rootDir = '.'
    for dirName, subdirList, fileList in os.walk(rootDir):
        for fname in fileList:
            ending = fname[fname.rfind("."):]
            if ending == ".py":
                should_add = True
                for excluded in LIST_OF_FILES_TO_NOT_ENCRYPT_OR_DECRYPT:
                    if excluded in fname:
                        should_add = False
                if should_add:
                    path = dirName + os.sep + fname
                    paths_to_files.append(path)
    return paths_to_files