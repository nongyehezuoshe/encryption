# encryption_with_args.py
from cryptography.fernet import Fernet
import hashlib
import base64
import os
import sys

def generate_key_from_password(password):
    key = hashlib.sha256(password.encode()).digest()
    encoded_key = base64.urlsafe_b64encode(key)
    return encoded_key

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    file_name, file_ext = os.path.splitext(file_path)
    output_file_path = file_name + '.encrypted'

    with open(output_file_path, 'wb') as f:
        f.write(encrypted_data)

def decrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(data)

    file_name, file_ext = os.path.splitext(file_path)

    if file_ext == '.encrypted':
        output_file_path = file_name + '.decrypted'
    else:
        output_file_path = file_path + '.decrypted'

    with open(output_file_path, 'wb') as f:
        f.write(decrypted_data)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: encryption <encrypt/decrypt> <file_path> <password>")
        sys.exit(1)

    action = sys.argv[1].lower()
    file_path = sys.argv[2]
    password = sys.argv[3]

    if action == 'encrypt':
        key = generate_key_from_password(password)
        encrypt_file(file_path, key)
        print("File encrypted successfully.")
    elif action == 'decrypt':
        key = generate_key_from_password(password)
        try:
            decrypt_file(file_path, key)
            print("File decrypted successfully.")
        except Exception as e:
            print("Decryption failed. Possibly incorrect password or file is corrupted.")
    else:
        print("Invalid choice. Please enter 'encrypt' or 'decrypt'.")