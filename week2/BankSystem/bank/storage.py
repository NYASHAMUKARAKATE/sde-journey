import pickle
import os
from pathlib import Path

class BankStorage:
    """Handles data persistence for bank accounts"""
    
    def __init__(self, filename="accounts.pkl"):
        self.data_dir = Path("data")
        self.data_dir.mkdir(exist_ok=True)
        self.filepath = self.data_dir / filename
    
    def save(self, accounts):
        """Save accounts to file"""
        try:
            with open(self.filepath, 'wb') as f:
                pickle.dump(accounts, f)
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False
    
    def load(self):
        """Load accounts from file"""
        if not self.filepath.exists():
            return {}
        
        try:
            with open(self.filepath, 'rb') as f:
                return pickle.load(f)
        except Exception as e:
            print(f"Error loading data: {e}")
            return {}