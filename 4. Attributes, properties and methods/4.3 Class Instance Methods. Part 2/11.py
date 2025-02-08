from typing import List


class Todo:
    def __init__(self):
        self.things = []

    def add(self, thing: str, priority: int):
        self.things.append((thing, priority))

    def get_by_priority(self, n: int) -> List[str]: 
        return [tpl[0] for tpl in self.things if n == tpl[1]]

    def get_low_priority(self) -> List[str]:
        if self.things:
            min_priority = min([tpl[1] for tpl in self.things])
            return [tpl[0] for tpl in self.things if tpl[1] == min_priority]
        return self.things

    def get_high_priority(self) -> List[str]:
        if self.things:
            max_priority = max([tpl[1] for tpl in self.things])
            return [tpl[0] for tpl in self.things if tpl[1] == max_priority]
        return self.things