def get_min(l: list[str]) -> str:
    p = l
    a = ''
    for i in p:
        if i == '0':
            continue
        a = i
        p.pop(p.index(i))
    return a + p[0]


def algo(n: int) -> bool:
    _max = int(get_min(sorted(str(n), reverse=True)))
    _min = int(get_min(sorted(str(n))))

    return 58 in (_min, _max, _max - _min)


print(algo(920))
c = 0
for i in range(100, 1000):
    c += algo(i)

print(c)
