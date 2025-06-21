import json
import pickle
import os

class BankStorage:
    def __init__(self, filename="accounts.pkl"):
        self.filename = filename

    def save(self, accounts):
        """Save accounts to file with error handling"""
        try:
            with open(self.filename, "wb") as f:
                pickle.dump(accounts, f)
            return True
        except Exception as e:
            print(f"Save error: {e}")
            return False

    def load(self):
        """Load accounts from file with error handling"""
        if not os.path.exists(self.filename):
            return {}
        try:
            with open(self.filename, "rb") as f:
                return pickle.load(f)
        except Exception as e:
            print(f"Load error: {e}")
            return {}