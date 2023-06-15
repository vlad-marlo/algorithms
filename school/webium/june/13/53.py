# (ДЕЛ(x, A) ∧ ДЕЛ(x, 21)) → ДЕЛ(x, 18)
def check(a: int, x: int) -> bool:
    return ((x % a == 0) and (x % 21 == 0)) <= (x % 18 == 0)


for a in range(1, 1000):
    if all(check(a, x) for x in range(1, 1000)):
        print(a)
        break