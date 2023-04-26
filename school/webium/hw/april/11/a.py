def read_data(filename: str) -> tuple[int, list[int]]:
    with open(filename) as file:
        n, m = map(int, file.readline().split())
        return m, [int(file.readline()) for _ in range(n)]


def solution(m: int, data: list[int]) -> int:
    start = 0
    end = 0
    s = data[start]
    res = 0
    while s + data[end + 1]<= m:
        s += data[end + 1]
        end += 1
    res = end + 1
    while start < len(data):
        s -= data[start]
        start += 1
        while end + 1 < len(data) and s + data[end + 1]<= m:
            s += data[end + 1]
            end += 1
        res = max(res, end - start + 1)
    return res


print(solution(*read_data('27A_1.txt')), end=' ')
print(solution(*read_data('27B_1.txt')))

