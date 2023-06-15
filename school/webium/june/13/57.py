# (X & 41 = 0) → ((X & 119 ≠ 0) → (X & A ≠ 0))

def check(a, x) -> bool:
    return (x & 41 == 0) <= ((x & 119 != 0) <= (x & a != 0))


for a in range(1, 1000):
    if all(check(a, x) for x in range(1, 1000)):
        print(a)
        break