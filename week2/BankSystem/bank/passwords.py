import hashlib
import secrets

def create_password(password):
    """Create a secure password hash with salt"""
    salt = secrets.token_hex(16)
    return {
        'hash': hashlib.sha256((password + salt).encode('utf-8')).hexdigest(),
        'salt': salt
    }

def verify_password(password, password_data):
    """Verify password against stored hash and salt"""
    if not password_data or 'hash' not in password_data or 'salt' not in password_data:
        return False
    test_hash = hashlib.sha256((password + password_data['salt']).encode('utf-8')).hexdigest()
    return test_hash == password_data['hash']