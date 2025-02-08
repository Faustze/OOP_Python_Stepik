from dataclasses import dataclass


@dataclass
class PiggyBank():
    content = 'coins'
    alternate_name = 'penny_bank'


money_box = PiggyBank()
