def read_data(filename: str) -> list[int]:
    with open(filename) as file:
        return [int(file.readline()) for _ in range(int(file.readline()))]


def pivot(data: list[int]) -> list[list[int]]:
    res = [[0 for _ in range(9)] for _ in range(len(data))]
    res[0][data[0] % 9] += 1
    for index, item in enumerate(data[1:], start=1):
        res[index][item % 9] = res[index - 1][item % 9] + 1
    return res


def solution(data: list[int]) -> int:
    count = 0
    forward = pivot(data)
    backward = pivot(data[::-1])[::-1]
    for i in range(len(forward) - 9):
        count += forward[i][data[i] % 9] * backward[i + 9][data[i + 9] % 9]
    return count


print(solution(read_data('27-A.txt')))
print(solution(read_data('27-B.txt')))
