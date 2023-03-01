def check(a: int, x: int) -> bool:
    return (x & 29 != 0) <= ((x & 12 == 0) <= (x & a != 0))


for a in range(1000):
    if all(check(a, x) for x in range(1000)):
        print(a)
        break
