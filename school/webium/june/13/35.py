# (x & a = 0) → ((x & 31 ≠ 0) → (x & 35 ≠ 0))


def check(a, x) -> bool:
    return (x & a == 0) <= ((x & 31 != 0) <= (x & 35 != 0))

for a in reversed(range(50, 121)):
    if all(check(a, x) for x in range(1, 1000)):
        print(a)
        break