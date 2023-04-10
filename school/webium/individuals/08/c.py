def read_data(filename: str) -> list[int]:
    with open(filename) as file:
        return [int(file.readline()) for _ in range(int(file.readline()))]


def solution(data: list[int]) -> int:
    n = len(data)
    o_i = n // 2
    sum_after = sum(data[o_i:])
    sum_before = sum(data[1:o_i])
    costs = [0] * n
    for i in range(1, n):
        costs[0] += min(n - i, i) * data[i]
    ans = costs[0]
    res = 1
    for i in range(1, n):
        sum_before += data[i - 1] - data[o_i]
        sum_after += data[o_i]
        costs[i] = costs[i-1] + sum_after - sum_before
        o_i = (o_i + 1) % n

    return -1


print(solution(read_data('27A_3.txt')))
print(solution(read_data('27B_3.txt')))
