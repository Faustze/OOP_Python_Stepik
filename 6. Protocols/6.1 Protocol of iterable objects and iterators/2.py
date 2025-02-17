class DevelopmentTeam:
    def __init__(self):
        self._seniors = []
        self._juniors = []

    def add_junior(self, *args):
        self._juniors.extend(args)

    def add_senior(self, *args):
        self._seniors.extend(args)

    def __iter__(self):
        for junior in self._juniors:
            yield (junior, 'junior')
        for senior in self._seniors:
            yield (senior, 'senior')


beegeek = DevelopmentTeam()
beegeek.add_junior('Timur')
beegeek.add_junior('Arthur', 'Valery')
beegeek.add_senior('Gvido')
print(*beegeek)