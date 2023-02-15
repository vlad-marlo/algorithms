def algo(a: int, x: int) -> bool:
    return (x & 41 == 0) <= ((x & 119 != 0) <= (x & a != 0))


for a in range(10000):
    if all(algo(a, x) for x in range(1, 1000)):
        print(a)
        break