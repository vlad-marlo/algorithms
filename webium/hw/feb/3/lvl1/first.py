def check(a: int, x: int) -> bool:
    return (a % 3 == 0) and ((x % 220) or ((a % x == 0) or (550 % x)))


for a in range(1, 1000):
    if all(check(a, x) for x in range(1, 10000)):
        print(a)
        break
