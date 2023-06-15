# ¬(x ∈ A) →¬((x ∈ {1, 2, 4, 8}) ∨ (x ∈ {1, 2, 3, 4, 5, 6}))
def check(x, a) -> int:
    return (x in a) or ((x not in [1, 2, 4, 8]) and (x not in (1, 2, 3, 4, 5, 6)))


A = set()
for i in range(-1000000, 100010):
    if not check(i, A):
        A.add(i)
    assert check(i, A)
print(len(A))
