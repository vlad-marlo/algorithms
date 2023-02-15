def check(a: int, x: int, y: int) -> bool:
    return ((5 * x - 6 * y) < a) or ((x - y) > 30)


for a in range(1000):
    if all(check(a, x, y) for x in range(1000) for y in range(1000)):
        print(a)
        break