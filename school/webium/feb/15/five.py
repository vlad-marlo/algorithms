def check(a: int, x: int) -> bool:
    return (x & a != 0) <= ((x & 10 == 0) <= (x & 3 != 0))


for a in range(1000):
    if all(check(a, x) for x in range(1000)):
        print(a)
