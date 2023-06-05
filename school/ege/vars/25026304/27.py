def read_data(filename: str) -> tuple[int, list[int]]:
    with open(filename) as file:
        return int(file.readline()), [int(file.readline()) for _ in range(int(file.readline()))]


def get_maxes(data: list[int], reverse: bool = False) -> list[int]:
    if reverse:
        data = data[::-1]
    res = [data[0]]
    for i in data[1:]:
        res.append(max(i, res[-1]))
    return res if not reverse else res[::-1]


def solution(k: int, data: list[int]) -> int:
    forward = get_maxes(data)
    backward = get_maxes(data, True)
    mx = 0
    for i in range(len(data) - k):
        mx = max(forward[i] + backward[i + k], mx)
    return mx


print(solution(*read_data('27_A_8513.txt')), end=' ')
print(solution(*read_data('27_B_8513.txt')))
