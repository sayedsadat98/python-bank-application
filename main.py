class BankAccount():

    def __init__(self, initial_balance: float):
        """
            Initializes a new BankAccount instance with an initial balance.
            Args:
                initial_balance (float): The initial balance of the account.
            Raises:
                ValueError: If the initial balance is negative.
        """
        if initial_balance < 0:
            raise ValueError("Initial Balance cannot be negative!")

        self.balance = initial_balance

    def deposit(self, amount: float):
        """
            Deposits a specified amount into the bank account.
            Args:
                amount (float): Non-negative amount to be deposited.
            Raises:
                ValueError: If the deposit amount is negative.
        """
        if amount < 0:
            raise ValueError("You must deposit a valid amount")

        self.balance = self.balance + amount
        print("Deposited Successfully!\nNew Balance: $", self.balance)

    def withdraw(self, amount: float):
        """
            Withdraws a specified amount from the bank account.
            Args:
                amount (float): The amount to withdraw.
            Raises:
                ValueError: If the withdrawal amount > current balance.
        """
        if amount > self.balance:
            raise ValueError("Insufficient Fund!")

        self.balance = self.balance - amount

    def get_balance(self) -> float:
        return self.balance


# Demo
if __name__ == '__main__':
    myBank = BankAccount(1000)
    myBank.deposit(1200)
    myBank.deposit(1200)
    print(myBank.get_balance())
    myBank.withdraw(100)
    print(myBank.get_balance())
