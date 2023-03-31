import math


def read_data(filename: str) -> list[int]:
    with open(filename) as file:
        return [int(x) for x in file.readlines()]


def solution(data: list[int]) -> tuple[int, int]:
    sm, count = 1000000, 0
    for i in range(len(data) - 1):
        a, b = data[i:i+2]
        if int(math.sqrt(a + b)) ** 2 == a + b and (a + b) % 4 == 0:
            sm = min(sm, a + b)
            count += 1
    return count, sm


print(*solution(read_data('17_2978.txt')))
