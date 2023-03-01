def check(a: int, x: int) -> bool:
    return ((x % 175) or (x % 25)) or ((2 * x + a) >= 1780)


print(min([a for a in range(10000) if all(check(a, x) for x in range(1, 10000))]))
