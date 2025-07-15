"""
Bank System Package

This package contains all the core banking functionality including:
- Account management (BankAccount, SavingsAccount)
- Password security
- Data storage
"""

from .core import BankAccount
from .savings import SavingsAccount
from .storage import BankStorage
from .passwords import create_password, verify_password

# Version of the bank package
__version__ = '1.0.0'

# List of what's available when importing from package
__all__ = [
    'BankAccount',
    'SavingsAccount',
    'BankStorage',
    'create_password',
    'verify_password'
]

# Package initialization code
print(f"Initializing Bank System Package v{__version__}")

# Create a default storage instance that can be imported
default_storage = BankStorage()