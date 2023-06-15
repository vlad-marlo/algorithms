# ((x & 26 ≠ 0) ∨ (x & 13 ≠ 0)) → ((x & 29 = 0) → (x & A ≠ 0))
def check(a, x):
    return ((x & 26 != 0) or (x & 13 != 0)) <= ((x & 29 == 0) <= (x & a != 0))


for a in range(1, 1000):
    if all(check(a, x) for x in range(1, 1000)):
        print(a)
        break
