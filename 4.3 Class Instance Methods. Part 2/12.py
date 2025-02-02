from typing import List


class Postman:
    def __init__(self):
        self.delivery_data = []

    def add_delivery(self, street: str, house: int, apartment: int):
        self.delivery_data.append((street, house, apartment))

    def get_houses_for_street(self, street: str) -> List[str]:
        return list({tpl[1] for tpl in self.delivery_data if tpl[0] == street})

    def get_flats_for_house(self, street: str, house: int) -> List[str]:
        return list({tpl[2] for tpl in self.delivery_data if tpl[0] == street and tpl[1] == house})
