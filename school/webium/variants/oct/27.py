def read_data(filename: str) -> list[tuple[int, int]]:
    with open(filename) as file:
        n = int(file.readline())
        res = []
        for _ in range(n):
            a, b = map(int, file.readline().split())
            res.append((a, b))
        return res


def solution(data: list[tuple[int, int]]) -> int:
    min_diff = 10**10
    s = 0
    for pair in data:
        a, b = sorted(pair)
        s += a
        if (b - a) % 5 != 0:
            min_diff = min(b - a, min_diff)
    if s % 5 == 0:
        return s + min_diff
    return s

print(solution(read_data('27A.txt')), end=' ')
print(solution(read_data('27B.txt')))
