# (x > 39) ∨ (y > 26) ∨ (2x + 4y < A)
def check(a, x, y) -> bool:
    return (x > 39) or (y > 26) or (2 * x + 4 * y < a)


for a in range(1000):
    if all(check(a, x, y) for x in range(100) for y in range(100)):
        print(a)
        break