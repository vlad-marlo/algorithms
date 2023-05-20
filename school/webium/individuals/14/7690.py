def read_data(filename: str) -> tuple[int, list[int]]:
    with open(filename) as file:
        n, k, m = map(int, file.readline().strip().split())
        data = {}
        for _ in range(n):
            key, val = map(int, file.readline().strip().split())
            if val >= k:
                data[key] = val
        res = [0 for _ in range(max(data) + 1)]
        for key, v in data.items():
            res[key] = v
        return m, res


def solution(m: int, data: list[int]) -> tuple[int, ...]:
    index = 0
    count = 0
    for i in range(len(data)):
        if data[i]:
            index = i
            break
    while index != len(data):
        for i in reversed(range(index + 1, index + m + 1)):
            if data[i]:
                index = i
                count += 1
                break
        else:
            break
    return count, index


print(*solution(*read_data('26_7690.txt')))
