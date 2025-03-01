from abc import ABC, abstractmethod


class ChessPiece(ABC):
    '''Шахматная доска'''
    def __init__(self, horizontal: str, vertical: int):
        self.horizontal, self.vertical = horizontal, vertical

    @abstractmethod
    def can_move(self):
        pass


class King(ChessPiece):
    def can_move(self, horizontal: str, vertical: int) -> bool:
        can = abs(ord(horizontal) - ord(self.horizontal)) + abs(vertical - self.vertical)
        return all(
            (
                abs(ord(horizontal) - ord(self.horizontal)) <= 1,
                abs(vertical - self.vertical) <= 1,
                can in (1, 2)
            )
        )


class Knight(ChessPiece):
    def can_move(self, horizontal: str, vertical: int) -> bool:
        return (ord(self.horizontal) - ord(horizontal)) ** 2 + (self.vertical - vertical) ** 2 == 5


kings = [King(h, v) for h in 'abcdefgh' for v in range(1, 9)]

for king in kings:
    print('*' * 20)
    for horizontal in 'abcdefgh':
        for vertical in range(1, 9):
            if king.can_move(horizontal, vertical):
                print(f'King({king.horizontal}{king.vertical})', f'{horizontal}{vertical}',
                      king.can_move(horizontal, vertical))

