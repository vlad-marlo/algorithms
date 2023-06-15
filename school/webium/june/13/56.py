# ¬(x ∈ A) → (¬(x ∈ {1, 12}) ∧ ¬(x ∈ {12, 13, 14, 15, 16}))

A = set()


def check(x) -> bool:
    return (x not in A) <= ((x not in (1, 12)) and (x not in (12, 13, 14, 15, 16)))

for a in range(1000):
    if not check(a):
        A.add(a)
print(len(A))
print(A)
