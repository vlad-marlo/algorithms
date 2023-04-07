def read_data(filename: str) -> list[int]:
    with open(filename) as file:
        n = int(file.readline())
        data = [0] * 10_000_000
        for _ in range(n):
            key, val = map(int, file.readline().strip().split())
            data[key] = val
        return data


def solution(data: list[int]) -> int:
    data = list(map(lambda x: x // 48 + int(x % 48 != 0), data))
    ans = 100 ** 100
    sm = sum(data)
    c = 0
    for i in range(1, len(data)):
        c += data[i] * i
    b = data[0]
    for i in range(1, len(data)):
        c += 2 * b - sm
        if data[i] != 0:
            ans = min(ans, c)
        b += data[i]
    return ans


print(solution(read_data('27A.txt')), end=' ')
print(solution(read_data('27B.txt')))
