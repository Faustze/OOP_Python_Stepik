from math import pi


class PiggyBank:
    def __init__(self, balance=0):
        self.balance = balance
        self.volume = 400

    def add_coins(self, coins):
        if self.balance + coins > self.volume:
            raise(ValueError('Копилка слишком мала!'))
        else:
            self.balance += coins

    def remove_coins(self, coins):
        if self.balance - coins < 0:
            raise(ValueError('В копилке недостаточно монет!'))
        else:
            self.balance -= coins


piggybank = PiggyBank()
piggybank.add_coins(400)
piggybank.remove_coins(500)
print(piggybank.balance)
