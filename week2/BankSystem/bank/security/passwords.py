"""Secret codes to protect accounts - like bank card PINs"""

import hashlib
import os

def create_password(password):
    """Turn your password into a secret code which is much safer"""
    salt = os.urandom(16)  # Extra random spice
    secret = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode(),
        salt,
        100000  # How many times we mix it
    )
    return f"{salt.hex()}:{secret.hex()}"

def check_password(stored_password, user_input):
    """Check if the password matches the correct one"""
    salt, secret = stored_password.split(':')
    salt = bytes.fromhex(salt)
    new_secret = hashlib.pbkdf2_hmac(
        'sha256',
        user_input.encode(),
        salt,
        100000
    )
    return new_secret.hex() == secret