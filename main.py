class BankAccount():

    def __init__(self, initial_balance: float):
        if initial_balance < 0:
            raise ValueError("Initial Balance cannot be negative!")

        self.balance = initial_balance

    def deposit(self, amount: float):
        if amount < 0:
            raise ValueError("You must deposit a valid amount")

        self.balance = self.balance + amount
        print("Deposited Successfully!\nNew Balance: $", self.balance)

    def withdraw(self, amount: float):
        if amount > self.balance:
            raise ValueError("Insufficient Fund!")

        self.balance = self.balance - amount

    def get_balance(self) -> float:
        return self.balance


if __name__ == '__main__':
    myBank = BankAccount(1000)
    myBank.deposit(1200)
    myBank.deposit(1200)
    print(myBank.get_balance())
    myBank.withdraw(100)
    print(myBank.get_balance())
