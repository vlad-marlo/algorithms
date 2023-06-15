# (2x + 3y ≠ 150) ∨ (x < A) ∧ (y < A)

def check(a, x, y) -> bool:
    return (2 * x + 3 * y != 150) or (x < a) and (y < a)


for a in range(1000):
    if all(check(a, x, y) for x in range(1000) for y in range(1000)):
        print(a)
        break