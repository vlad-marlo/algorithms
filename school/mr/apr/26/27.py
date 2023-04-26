def read_data(filename: str) -> tuple[int, list[int]]:
    with open(filename) as file:
        return int(file.readline()), [int(file.readline()) for _ in range(int(file.readline()))]


def pivot(data: list[int]) -> list[int]:
    res = [data[0]]
    for i in data[1:]:
        res.append(max(i, res[-1]))
    return res


def solution(k: int, data: list[int]) -> int:
    indexes = [0] * len(data)
    mx = 0
    for i in range(len(data)):
        if data[i] % k == 0:
            indexes[i] = i
        elif i == 0:
            continue
        else:
            indexes[i] = indexes[i-1]
    forward = pivot(data)
    backward = pivot(data[::-1])[::-1]
    for i in range(len(data)):
        mx = max(mx, forward[i] + backward[indexes[i]-1])
    return mx


print(solution(*read_data("27A_7856.txt")))
print(solution(*read_data("27B_7856.txt")))
