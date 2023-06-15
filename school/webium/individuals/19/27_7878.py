MAGIC_CONST = 157


def read_data(filename: str) -> tuple[int, list[int]]:
    with open(filename) as file:
        n, k = map(int, (file.readline() for _ in range(2)))
        return k, [int(file.readline()) for _ in range(n)]


def get_maxes(data: list[int], reverse=False) -> list[list[int]]:
    if reverse:
        data = data[::-1]
    maxes = [10**10 for _ in range(MAGIC_CONST)]
    maxes[data[0] % MAGIC_CONST] = data[0]
    res = [maxes]
    for i in data[1:]:
        new = res[-1].copy()
        new[i % MAGIC_CONST] = min(new[i % MAGIC_CONST], i)
        res.append(new)
    return res if not reverse else res[::-1]


def solution(min_distance: int, data: list[int]) -> int:
    forwards, backwards = get_maxes(data), get_maxes(data, True)
    ans = 10**10
    for i in range(len(data) - min_distance):
        ans = min(ans, forwards[i][0] * min(backwards[i+min_distance]), min(forwards[i]) * backwards[i+min_distance][0])
    return ans


print(solution(*read_data('27A_7878.txt')))
print(solution(*read_data('27B_7878.txt')))
