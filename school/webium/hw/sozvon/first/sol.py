def read_data() -> tuple[list[tuple[int, int, bool]], int]:
    with open('26_2.txt') as f:
        _count, _money_limit = map(int, f.readline().strip().split())
        res: list[tuple[int, int, bool]] = []
        for _ in range(_count):
            row, price, category = f.readline().strip().split()
            res.append((int(row), int(price), "C" in category))
        return res, _money_limit


def solution(data: list[tuple[int, int, bool]], limit: int) -> tuple[int, int]:
    prices: list[tuple[float, int, bool]] = []
    for row, num, provide_discount in data:
        if not provide_discount:
            prices.append((num, num, False))
        else:
            prices.append((num * (1 - ((row % 100) / 100)), num, True))
    prices.sort(key=lambda x: x[0])
    answer = 0
    max_price = 0
    for a, b, _ in prices:
        if (res := answer + a) <= limit:
            answer = res
            max_price = a
        else:
            break
    new = limit - (int(answer+0.5) - max_price)
    discount = [int(i) for i, _, d in prices if d]
    for i in reversed(range(int(new))):
        if i in discount:
            return int(answer), i
    return int(answer), 0


assert solution([(1, 200, False), (2, 300, True), (3, 150, False), (4, 270, False), (5, 350, False), (6, 240, True), (7, 200, True), (8, 300, True),], 820) == (761, 276)
print(*solution(*read_data()))

