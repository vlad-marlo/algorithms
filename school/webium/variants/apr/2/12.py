def algo(n: int) -> str:
    s = '3' + n * '5'
    while '25' in s or '355' in s or '555' in s:
        s = s.replace('25', '3', 1).replace('355', '52', 1).replace('555', '23', 1)
    return s


for i in range(1000):
    sm = sum([int(x) for x in algo(i)])
    if sm == 27:
        print(i)
        break
    # print(i, sm)
    # print(i, sum([int(x) for x in algo(i)]))
print(algo(4), algo(5))