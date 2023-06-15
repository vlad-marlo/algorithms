# (x & 49 = 0) → ((x & 28 ≠ 0) → (x & А ≠ 0))

def check(a, x) -> bool:
    return (x & 49 == 0) <= ((x & 28 != 0) <= (x & a != 0))


for a in range(1000):
    if all(check(a, x) for x in range(1000)):
        print(a)
        break