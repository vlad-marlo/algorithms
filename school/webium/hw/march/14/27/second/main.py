def read_data(filename: str) -> list[tuple[int, ...]]:
    with open(filename) as file:
        return [tuple(map(int, file.readline().split())) for _ in range(int(file.readline()))]


def solution(data: list[tuple[int, ...]]) -> int:
    d = 10 ** 10
    summ = 0
    for a, b in data:
        summ += min(a, b)
        if abs(a - b) % 5 != 0:
            d = min(d, abs(a - b))
    if summ % 5 != 0:
        return summ
    return summ + d


assert solution([(1, 3), (5, 12), (6, 9), (5, 4), (3, 3), (1, 1)]) == 21
print(solution(read_data('27_A.txt')))
print(solution(read_data('27_B.txt')))
