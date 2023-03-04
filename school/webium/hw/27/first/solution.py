import math


def read_data(file: str) -> list[int]:
    with open(file) as f:
        return [int(f.readline()) for _ in range(int(f.readline()))]


def solution(data: list[int]) -> int:
    idx = [i for i in range(len(data)) if (int(math.sqrt(data[i])) ** 2 == data[i] and data[i] != 1) or i == 0]
    print(idx)
    return max([idx[i + 1] - idx[i] for i in range(len(idx) - 1)])


print(solution(read_data('27_a.txt')))
# print(solution(read_data('27_b.txt')))
