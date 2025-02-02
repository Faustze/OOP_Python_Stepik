class BankAccount:
    def __init__(self, balance: int = 0):
        self._balance = balance

    def get_balance(self) -> int | float:
        return self._balance

    def deposit(self, amount: int | float):
        self._balance += amount

    def withdraw(self, amount: int | float):
        if amount > self._balance:
            raise (ValueError('На счете недостаточно средств'))
        else:
            self._balance -= amount

    def transfer(self, account, amount: int | float):
        self.withdraw(amount)
        account.deposit(amount)