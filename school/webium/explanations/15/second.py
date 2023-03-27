def check(a, x, y, z) -> bool:
    return (x | 50 == x) or (y & 34 != 0) or (z | 24 != 24) or (x * y * z > a // 8)


for a in reversed(range(100)):
    if all(check(a, x, y, z) for x in range(1, 100) for y in range(1, 100) for z in range(1, 100)):
        print(a)
        break
