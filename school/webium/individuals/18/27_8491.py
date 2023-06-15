def read_data(filename: str) -> tuple[int, int, list[int]]:
    with open(filename) as file:
        n, k, m = int(file.readline()), int(file.readline()), int(file.readline())
        return k, m, [int(file.readline()) for _ in range(n)]


def solution(k: int, m: int, data: list[int]) -> int:
    maxes = [0 for _ in range(m)]
    ans = 0
    i1 = 0
    for i in range(len(data) - k * (m + 1)):
        if i1 - i < k:
            i1 = i
            for n in range(m):
                maxes[n] = max(data[i1 + k * (n - 1):-1 * k * (n - 1)] or [data[-1]])
                i1 = data.index(maxes[n], i1 + k if i1 + k < len(data) else i1)
        ans = max(ans, sum(maxes) + data[i])
    return ans


print(solution(*read_data('27a_8491.txt')))
print(solution(*read_data('27b_8491.txt')))
