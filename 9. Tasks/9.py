class TicTacToe:
    def __init__(self):
        self._area = [[' ' for _ in range(3)] for _ in range(3)]
        self._player = 'X'
        self._move = 0

    def mark(self):
        pass

    def show(self):
        field = ['|'.join(self._area[r]) for r in range(3)]
        print(*('\n-----\n'.join(field)), sep='')