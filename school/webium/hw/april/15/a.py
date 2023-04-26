def read_data(filename: str) -> list[int]:
    with open(filename) as file:
        data = [0 for _ in range(10_000_000)]
        for _ in range(int(file.readline())):
            key, val = map(int, file.readline().strip().split())
            data[key] = val
        return data


def solution(data: list[int]) -> int:
    data = list(map(lambda x: x // 48 + int(x % 48 != 0), data))
    sm = sum(data)
    c = 0
    for i in range(len(data)):
        c += i * data[i]
    ans = c
    b = data[0]
    for i in data[1:]:
        c += 2 * b - sm
        if i != 0:
            ans = min(ans, c)
        b += i
    return ans


print(solution(read_data('27A_2.txt')), end=' ')
print(solution(read_data('27B_2.txt')))
print(solution(read_data('test.txt')))
