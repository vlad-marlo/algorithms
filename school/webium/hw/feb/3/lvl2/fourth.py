def check(a: int, x: int) -> bool:
    return ((x % 3) or (x % 5)) or ((x + a) >= 70)


print(min([a for a in range(1000) if all(check(a, x) for x in range(1, 1000))]))
