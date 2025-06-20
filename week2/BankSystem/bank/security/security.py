import hashlib
import os

def hash_password(password):
    """Hash a password with a randomly generated salt"""
    salt = os.urandom(16)
    pwd_hash = hashlib.sha256(salt + password.encode()).hexdigest()
    return salt.hex() + pwd_hash

def verify_password(hashed_password, input_password):
    """Verify a stored password against one provided by user"""
    salt = bytes.fromhex(hashed_password[:32])
    stored_hash = hashed_password[32:]
    input_hash = hashlib.sha256(salt + input_password.encode()).hexdigest()
    return input_hash == stored_hash