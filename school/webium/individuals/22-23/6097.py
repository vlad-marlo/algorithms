def read_data(filename: str) -> tuple[int, list[int]]:
    with open(filename) as file:
        n, m = map(int, file.readline().strip().split())
        return m, [int(file.readline()) for _ in range(n)]


def solution(m: int, data: list[int]) -> int:
    data *= 2
    sm = sum(data[:2 * m + 1])
    res = sm
    for i in range(2 * m + 1, len(data)):
        sm += data[i] - data[i - 2 * m - 1]
        res = max(res, sm)
    return res


print(solution(*read_data('27A_6318.txt')))
print(solution(*read_data('27B_6318.txt')))
