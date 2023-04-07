def read_data(filename: str) -> list[int]:
    with open(filename) as file:
        d = [0] * 10_000_000
        for _ in range(int(file.readline())):
            key, val = map(int, file.readline().strip().split())
            d[key] = val
        return d


def solution(data: list[int]) -> int:
    data = list(map(lambda x: x // 44 + int(x % 44 > 0), data))
    sm = sum(data)
    c = 0
    for i in range(len(data)):
        c += i * data[i]
    b = data[0]
    ans = 10000000000000**1000
    for i in range(1, len(data)):
        c += 2 * b - sm
        if data[i]:
            ans = min(c, ans)
        b += data[i]
    return ans


print(solution(read_data('27_A_7097.txt')))
print(solution(read_data('27_B_7097.txt')))

