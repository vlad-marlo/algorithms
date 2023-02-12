def res(a: int, x: int) -> bool:
    return (x & 25 != 0) <= ((x & 17 == 0) <= (x & a != 0))


for a in range(1, 1000):
    if all(res(a, x) for x in range(1, 1000)):
        print(a)
        break
