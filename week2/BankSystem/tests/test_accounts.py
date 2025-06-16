"""Make sure nothing breaks - like bank auditors"""

from bank.accounts.core import BankAccount

def test_deposit():
    """Does depositing money work?"""
    acc = BankAccount("Test", 100)
    acc.deposit(50)
    assert acc.balance == 150

def test_withdraw():
    """Can we take money out?"""
    acc = BankAccount("Test", 100)
    acc.withdraw(20)
    assert acc.balance == 80