# ((x^2 > 16) ∨ (A > x)) ∧ ((y^2 ≤ 81) ∨ (A ≤ y))
def check(a, x, y) -> bool:
    return ((x ** 2 > 16) or (a > x)) and ((y ** 2 <= 81) or (a <= y))


for a in range(1000):
    if all(check(a, x, y) for x in range(1000) for y in range(1000)):
        print(a)