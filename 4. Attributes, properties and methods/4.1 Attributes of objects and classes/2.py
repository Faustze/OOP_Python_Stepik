class PiggyBank:
    pass


money_box1 = PiggyBank()
money_box2 = PiggyBank()

setattr(money_box1, 'coins', 10)
setattr(money_box2, 'coins', 15)
setattr(money_box2, 'color', 'pink')

print(money_box2.__dict__)
