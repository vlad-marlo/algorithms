def algo(s: int) -> int:
    n = 4
    while s < 37:
        s += 3
        n *= 2
    return n


for i in range(-1000, 10000):
    if algo(i) == 128:
        print(i)
