# Nathan Park
# nyp5aa

from cryptography.fernet import Fernet
from helpers import generate_sym_key, get_files

def main():
    files = get_files()
    key = generate_sym_key()
    decrypt_files(files, key)
    return


def decrypt_files(files, key):
    fernet = Fernet(key)
    for file in files:
        # Get data from encrypted file
        with open(file, 'rb') as f:
            data = f.read()

        # Decrypt the data
        decrypted = fernet.decrypt(data)

        # Write message to files
        with open(file, 'wb') as f:
            f.write(decrypted)


if __name__ == "__main__":
    main()