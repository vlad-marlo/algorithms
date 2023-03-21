def read_data() -> tuple[int, list[tuple[int, int]]]:
    with open('26_5.txt') as f:
        _time: int
        c, _time = map(int, f.readline().split())
        ans = []
        for _ in range(c):
            a, b = map(int, f.readline().split())
            ans.append((a, b))
        return _time, ans


def solution(time: int, data: list[tuple[int, int]]) -> tuple[int, int]:
    difficulties = [a for a, _ in data]
    avg = sum(difficulties) / len(difficulties)
    super_v = list(filter(lambda x: x[0] > avg, data))
    normal = list(filter(lambda x: x[0] <= avg, data))
    super_v.sort(key=lambda x: x[1])
    normal.sort(key=lambda x: x[1])
    count = 0
    duration = 0
    last_super = (0, 0)
    lastNormal = True
    for i in range(max(len(normal), len(super_v))):
        try:
            if time - (sup := super_v[i][1]) >= 0 and lastNormal:
                time -= sup
                count += 1
                duration += sup
                last_super = super_v[i]
                lastNormal = False
        except Exception:
            pass
        try:
            if time - (sup := normal[i][1]) >= 0:
                time -= sup
                count += 1
                lastNormal = True
        except Exception:
            pass
    if not lastNormal:
        count -= 1
        duration -= last_super[1]
    return count, duration


print(*solution(*read_data()))
print(*solution(50, [(7, 13), (9, 20), (4, 3), (8, 9), (5, 5)]))
