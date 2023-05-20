def read_data(filename: str) -> tuple[int, list[int]]:
    with open(filename) as file:
        n = int(file.readline())
        return int(file.readline()), [int(file.readline()) for _ in range(n)]


def get_counts(data: list[int]) -> list[list[int]]:
    res = [[0 for _ in range(25)]]
    res[0][data[0] % 25] += 1
    for i in data[1:]:
        res.append(res[-1])
        res[-1][i % 25] += 1
    return res


def solution(k: int, data: list[int]) -> int:
    count = 0
    for n1 in range(len(data) - k):
        for n2 in range(n1 + k, len(data)):
            if (data[n1] + data[n2]) % 25 == 0:
                count += 1
    return count


print(solution(*read_data('27_test')))
print(solution(*read_data('27A.txt')))
print(solution(*read_data('27B.txt')))
