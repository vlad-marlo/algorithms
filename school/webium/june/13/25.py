# ДЕЛ(x, A) → (ДЕЛ(x, A) → ДЕЛ(x, 34) ∧ ДЕЛ(x, 51))

def check(a, x) -> bool:
    return (x % a == 0) <= ((x % a == 0) <= (x % 34 == 0) and (x % 51 == 0))


for a in range(1, 1000):
    if all(check(a, x) for x in range(1000)):
        print(a)
