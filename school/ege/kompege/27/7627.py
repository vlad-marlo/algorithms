def read_data(filename: str) -> tuple[int, list[int]]:
    with open(filename) as file:
        c, n = map(int, (file.readline() for _ in range(2)))
        return c, [int(file.readline()) for _ in range(n)]


def get_maxes(data: list[int]) -> list[int]:
    maxes = [data[0]]
    mx = data[0]
    for i in data[1:]:
        mx = max(mx, i)
        maxes.append(mx)
    return maxes


def solution(c: int, data: list[int]) -> int:
    maxes_reversed = get_maxes(data[::-1])[::-1]
    maxes = get_maxes(data)
    mx = 0
    for i in range(len(data) - c - 1):
        mx = max(maxes[i] + maxes_reversed[i+c+1], mx)
    return mx


print(solution(*read_data('27_A_7627.txt')), end=' ')
print(solution(*read_data('27_B_7627.txt')))
