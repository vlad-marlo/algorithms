def read_data() -> list[int]:
    with open('26_1.txt') as f:
        _ = f.readline()
        return list(map(int, f.readlines()))


def solution(data: list[int]) -> tuple[int, int]:
    res = {}
    for i in data:
        key = (i + 1) // 500
        if res.get(key) is None:
            res[key] = []
        res[key].append(i)
    ans = 0
    m = 0
    for val in res.values():
        val.sort()
        skid = list(map(lambda x: x * 0.5, val[:len(val)//2]))
        ans += sum(skid)
        if len(skid) == 0:
            skid = [0]
        m = max(m, max(skid))
    return int(ans), int(m)


print(*solution(read_data()))
assert solution([100, 50, 15, 160, 500, 1002, 2003, 2010, 2350, 2400]) == (2039, 1005)
