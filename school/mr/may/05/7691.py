def read_data(filename: str) -> list[int]:
    with open(filename) as file:
        n, m = map(int, file.readline().strip().split())
        data = [0] * m
        for _ in range(n):
            key, val = map(int, file.readline().strip().split())
            data[key - 1] = val * 2
        return data


def solution(data: list[int]) -> int:
    sm = sum(data)
    c = 0
    for i in range(len(data)):
        c += (i + 1) * data[i]
    ans = c
    ans_i = 0
    b = data[0]
    for i, item in enumerate(data):
        c += sm - 2 * b
        if item != 0:
            if c > ans:
                ans_i = i
                ans = c
            if c == ans:
                ans_i = max(ans_i, i)
        b += item
    return ans_i


print(solution(read_data('27A_7691.txt')))
print(solution(read_data('27B_7691.txt')))
