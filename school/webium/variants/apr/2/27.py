def read_data(filename: str) -> tuple[int, list[int]]:
    with open(filename) as file:
        n = int(file.readline())
        k = int(file.readline())
        return k, [int(file.readline()) for _ in range(n)]


def maxes(data: list[int]) -> list[int]:
    res = [data[0]]
    for i in data[1:]:
        res.append(max(res[-1], i))
    return res


def solution(k: int, data: list[int]) -> int:
    forward = maxes(data)
    backwards = maxes(data[::-1])[::-1]
    mx = 0
    for i in range(len(data) - k):
        mx = max(mx, forward[i] + backwards[i + k])
    return mx


print(solution(3, [10, 15, 100, 1, 30]))
print(solution(*read_data('27A.txt')), end=' ')
print(solution(*read_data('27B.txt')))
