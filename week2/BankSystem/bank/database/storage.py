import json

class BankStorage:
    def __init__(self, file="accounts.json"):
        self.file = file
        
    def save(self, accounts):
        """Save accounts to file with error handling"""
        try:
            with open(self.file, 'w') as f:
                # Only save essential data
                data = {
                    name: {
                        "owner": acc.owner,
                        "balance": acc.balance,
                        "type": type(acc).__name__
                    }
                    for name, acc in accounts.items()
                }
                json.dump(data, f, indent=2)
            return True
        except Exception as e:
            print(f"Save failed: {e}")
            return False