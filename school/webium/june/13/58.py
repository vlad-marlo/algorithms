# ДЕЛ(A, 3) ∧ (ДЕЛ(220, x) → (¬ДЕЛ(A, x) → ¬ДЕЛ(550, x)))

def check(a, x) -> bool:
    return (a % 3 == 0) and ((220 % x == 0) <= ((a % x != 0) <= (550 % x != 0)))


for a in range(1, 1000):
    if all(check(a, x) for x in range(1, 1000)):
        print(a)