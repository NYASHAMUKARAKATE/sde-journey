"""Where we keep permanent records - like file cabinets"""

import json
from pathlib import Path

class BankStorage:
    def __init__(self, file="accounts.json"):
        self.file = Path(file)
        
    def save(self, accounts):
        
        data = {
            acc.owner: {
                "balance": acc.balance,
                "history": acc.history
            }
            for acc in accounts.values()
        }
        with open(self.file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load(self):
        if not self.file.exists():
            return {}
            
        with open(self.file) as f:
            return json.load(f)