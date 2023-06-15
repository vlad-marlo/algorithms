# (A > y) ∨ (3x + 2y > 53) ∨ (A > x)
def check(a, x, y) -> bool:
    return (a > y) or (3 * x + 2 * y > 53) or (a > x)


for a in range(1000):
    if all(check(a, x, y) for x in range(1000) for y in range(1000)):
        print(a)
        break
