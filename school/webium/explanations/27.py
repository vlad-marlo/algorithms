def read_data(filename: str) -> list[tuple[int, ...]]:
    with open(filename) as file:
        return [tuple(sorted(map(int, file.readline().split()))) for _ in range(int(file.readline()))]


def solution(data: list[tuple[int, ...]]) -> int:
    sum_a = sum_b = sum_max = 0
    min_razn = 100000000
    for i in data:
        a, b, c = i
        sum_max += c
        sum_a += a
        sum_b += b
        min_razn = min(c - b, min_razn) if c - b % 2 != 0 else min_razn
    if sum_b % 2 == sum_a % 2:
        return sum_max - min_razn
    return sum_max


print(solution(read_data('27-A.txt')), solution(read_data('27-B.txt')))
#541 300229428