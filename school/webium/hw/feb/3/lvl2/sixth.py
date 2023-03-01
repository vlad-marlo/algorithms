def check(a: int, x: int) -> bool:
    return ((x % 6) or (x % 14)) or ((x + a) >= 70) and (a % 20 == 0)


for a in range(0, 100000, 20):
    if all(check(a, x) for x in range(1, 1000)):
        print(a)
        break
