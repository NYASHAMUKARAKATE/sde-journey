"""Watches for suspicious activity - like bank guards"""

class FraudMonitor:
    def __init__(self):
        self.suspicious_activity = []
    
    def check_transaction(self, account, amount):
        """Flag weird transactions"""
        if amount > 10000:  # Large transactions
            self.suspicious_activity.append(
                f"Large ${amount} transaction on {account}"
            )
        elif amount <= 0:  # Weird amounts
            self.suspicious_activity.append(
                f"Strange ${amount} attempt on {account}"
            )