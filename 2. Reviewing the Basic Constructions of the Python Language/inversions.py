from typing import Sequence


def inversions(sequence: Sequence[int]) -> int:
    inversions_list = []
    for i in range(len(sequence) - 1):
        for j in range(i + 1, len(sequence)):
            if sequence[i] > sequence[j]:
                inversions_list.append((sequence[i], sequence[j]))

    return len(inversions_list)


print(inversions([3, 1, 4, 2]))     # 3
print(inversions([1, 2, 3, 4, 5]))  # 0
print(inversions([4, 3, 2, 1]))     # 6
