def check(a: int, x: int, y: int) -> bool:
    return ((7 * y + x) < a) or ((2 * x + 3 * y) > 98)


for a in range(10000):
    if all(check(a, x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
        break
