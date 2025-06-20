import hashlib

def create_password(password):
    """Hash a password for storing."""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def verify_password(password, password_hash):
    """Verify a password against the stored hash."""
    return create_password(password) == password_hash