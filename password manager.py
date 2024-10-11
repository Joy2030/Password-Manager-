import secrets
import string

def generate_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password
from cryptography.fernet import Fernet

# Generate a key for encryption
def generate_key():
    return Fernet.generate_key()

# Encrypt the password
def encrypt_password(key, password):
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode())
    return encrypted_password

# Decrypt the password
def decrypt_password(key, encrypted_password):
    fernet = Fernet(key)
    decrypted_password = fernet.decrypt(encrypted_password).decode()
    return decrypted_password
import json
import os

# File to store user credentials
CREDENTIALS_FILE = "credentials.json"

# Save credentials to file
def save_credentials(username, encrypted_password):
    if os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, 'r') as file:
            credentials = json.load(file)
    else:
        credentials = {}
    
    credentials[username] = encrypted_password.decode()
    
    with open(CREDENTIALS_FILE, 'w') as file:
        json.dump(credentials, file, indent=4)

# Load credentials from file
def load_credentials():
    if os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, 'r') as file:
            credentials = json.load(file)
        return credentials
    else:
        return {}

# Retrieve stored password for a user
def retrieve_password(username, key):
    credentials = load_credentials()
    encrypted_password = credentials.get(username)
    if encrypted_password:
        return decrypt_password(key, encrypted_password.encode())
    else:
        return None
def main():
    print("Password Management System")
    
    # Generate a key for encryption
    key = generate_key()
    print(f"Generated Encryption Key: {key.decode()}")

    # Generate a secure password
    password = generate_password()
    print(f"Generated Password: {password}")

    # Encrypt the password
    encrypted_password = encrypt_password(key, password)
    print(f"Encrypted Password: {encrypted_password.decode()}")

    # Store the credentials
    username = "user1"
    save_credentials(username, encrypted_password)
    print(f"Credentials for {username} saved successfully.")

    # Retrieve and decrypt the password
    retrieved_password = retrieve_password(username, key)
    if retrieved_password:
        print(f"Retrieved Password for {username}: {retrieved_password}")
    else:
        print(f"No credentials found for {username}")

if __name__ == "__main__":
    main()

