def read_data(filename: str) -> tuple[int, list[int]]:
    with open(filename) as file:
        n, m = map(int, file.readline().strip().split())
        res = [0 for _ in range(10 ** 7)]
        # print(n, m)
        for i in range(n):
            key, val = map(int, file.readline().strip().split())
            res[key] = val
        return m, res


def solution(m: int, data: list[int]) -> int:
    data = list(map(lambda x: x // 30 + (x % 30 > 0), data))
    sm = sum(data[:2 * m + 1]) - data[m]
    res = 0 if data[m] == 0 else sm
    for i in range(2 * m + 1, len(data)):
        sm += data[i] - data[i - 2 * m - 1] + data[i - m - 1] - data[i - m]
        res = max(res, sm if data[i - m] else 0)
    return res


print(solution(*read_data('27_A_7275.txt')))
print(solution(*read_data('27_B_7275.txt')))
