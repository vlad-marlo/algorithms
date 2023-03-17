def read_data() -> tuple[dict[str, list[tuple[int, int, bool]]], int, int]:
    with open('26_2.txt') as file:
        _count, _money_limit = map(int, file.readline().strip().split())
        _data: dict[str, list[tuple[int, int, bool]]] = {}
        for _ in range(_count):
            number: int
            price: int
            category: str
            number, price, category = file.readline().split()
            status: bool = "C" in category
            category = category.replace("C", "")
            number, price = map(int, (number, price))
            if _data.get(category) is None:
                _data[category] = []
            _data[category].append((number, price, status))
        return _data, _count, _money_limit


def solution(data: dict[str, list[tuple[int, int, bool]]], count: int, limit: int) -> tuple[int, int]:
    _data: list[tuple[int, int]] = []
    for _, v in data.items():
        for row, num, has_discount in v:
            if has_discount:
                _data.append((int(num * (1 - ((row % 100) / 100))), num))
            else:
                _data.append((num, num))
    _data.sort(key=lambda x: x[0])
    _ans = 0
    max_min = 0
    for after, before in _data:
        if (res := (_ans + after)) <= limit:
            _ans = res
            if after != before:
                max_min = max(max_min, after)
        else:
            return _ans, max_min
    return _ans, max_min


print(*solution(*read_data()))
