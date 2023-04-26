def read_data(filename: str) -> list[tuple[int, int, int]]:
    with open(filename) as file:
        n = int(file.readline())
        res = []
        for _ in range(n):
            start, end, cost = map(int, file.readline().strip().split())
            res.append((start, end, cost))
        return res


def solution(goal: int, data: list[tuple[int, ...]]) -> tuple:
    data.sort(key=lambda x: (x[2], x[0], -x[1]))
    now = 0
    count = 0
    works = [0 for _ in range(2880)]
    while now < goal:
        line = data.pop()
        start, end, price = line
        for i in range(start, start + end):
            works[i] += 1
        now += price
        count += 1
    return count, max(works)


print(*solution(300_000, read_data('26_7756.txt')))
print(*solution(1000, read_data('test_7756')))
