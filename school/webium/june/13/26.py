# (ДЕЛ(x, A) ∧ ДЕЛ(x, 24) ∧ ¬ДЕЛ(x, 16)) → ¬ДЕЛ(x, A)

def check(a, x) -> bool:
    return ((x % a == 0) and (x % 24 == 0) and (x % 16 != 0)) <= (x % a != 0)


for a in range(1, 1000):
    if all(check(a, x) for x in range(1, 1000)):
        print(a)
