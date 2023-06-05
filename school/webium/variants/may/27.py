def read_data(filename: str) -> tuple[int, list[int]]:
    with open(filename) as file:
        n = int(file.readline())
        return int(file.readline()), [int(file.readline()) for _ in range(n)]


def get_counts(data: list[int]) -> list[list[int]]:
    res = [[0 for _ in range(25)]]
    res[0][data[0] % 25] += 1
    for i in data[1:]:
        s = res[-1].copy()
        s[i % 25] += 1
        res.append(s)
    return res


def sol(k: int, data: list[int]) -> int:
    backwards = get_counts(data[::-1])[::-1]
    ans = 0
    for i in range(k, len(data)):
        ans += backwards[i][(25 - data[i - k]) % 25]
    return ans
 

def solution(k: int, data: list[int]) -> int:
    count = 0
    for n1 in range(len(data) - k):
        for n2 in range(n1 + k, len(data)):
            if (data[n1] + data[n2]) % 25 == 0:
                count += 1
    return count


print(sol(*read_data('27_test')))  # 4
print(sol(*read_data('27A.txt')))  # 9773
print(sol(*read_data('27B.txt')))  #
print(solution(*read_data('27_test')))  # 4
print(solution(*read_data('27A.txt')))  # 9773
print(solution(*read_data('27B.txt')))  #
