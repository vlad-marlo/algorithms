def check(x: int) -> bool:
    m = 0
    n = 0
    while x % 2 == 0:
        x //= 2
        m += 1
    if m % 2 != 0:
        return False
    while x % 3 == 0:
        x //= 3
        n += 1
    return x == 1 and n % 2 != 0


for num in range(200_000_000, 400_000_001):
    if check(num):
        print(num)
