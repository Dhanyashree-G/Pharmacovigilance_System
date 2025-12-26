from cryptography.fernet import Fernet
import hashlib

KEY = Fernet.generate_key()
cipher = Fernet(KEY)

def encrypt(text):
    return cipher.encrypt(text.encode()).decode()

def decrypt(text):
    return cipher.decrypt(text.encode()).decode()

def hash_token(token):
    return hashlib.sha256(token.encode()).hexdigest()
