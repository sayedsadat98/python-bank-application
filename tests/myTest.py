import pytest
from main import BankAccount


class TestBankAccount:
    def test_create_account(self):
        account = BankAccount(1000)
        assert account.get_balance() == 1000

    def test_deposit(self):
        account = BankAccount(1000)
        account.deposit(500)
        assert account.get_balance() == 1500

    def test_withdraw(self):
        account = BankAccount(1000)
        account.withdraw(300)
        assert account.get_balance() == 700

    def test_withdraw_insufficient_funds(self):
        account = BankAccount(1000)
        with pytest.raises(ValueError, match="Insufficient Fund!"):
            account.withdraw(2000)

    def test_deposit_negative_amount(self):
        account = BankAccount(1000)
        with pytest.raises(ValueError, match="You must deposit a valid amount"):
            account.deposit(-200)

    def test_create_account_negative_balance(self):
        with pytest.raises(ValueError, match="Initial Balance cannot be negative!"):
            BankAccount(-100)
