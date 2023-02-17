def check(a: int, x: int) -> bool:
    return (x & 30 != 4) or ((x & 35 == 1) <= (x & a == 0))


for a in range(10000):
    if all(check(a, x) for x in range(10000)):
        print(a)
