# (х & 94 ≠ 0)→ ((x & 21 = 0)→ (x & A ≠ 0))

def check(a, x) -> bool:
    return (x & 94 != 0) <= ((x & 21 == 0) <= (x & a != 0))


for a in range(1, 1000):
    if all(check(a, x) for x in range(1, 1000)):
        print(a)
        break