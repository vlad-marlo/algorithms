# (3x + 4y ≠ 60) ∨ ((A ≥ x) ∧ (A ≥ y))
def check(a, x, y):
    return ((3 * x + 4 * y) != 60) or ((a >= x) and (a >= y))


for a in range(10000):
    if all(check(a, x, y) for y in range(1000) for x in range(1000)):
        print(a)
        break
