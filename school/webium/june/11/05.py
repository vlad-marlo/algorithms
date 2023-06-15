def algo(s: str) -> str:
    while '555' in s or '25' in s or '355' in s:
        s = s.replace('25', '3', 1)
        s = s.replace('355', '52', 1)
        s = s.replace('555', '23', 1)
    return s


for n in range(1, 10000):
    x = '3' + '5' * n
    res = algo(x)
    if sum(map(int, res)) == 27:
        print(n)
        break
