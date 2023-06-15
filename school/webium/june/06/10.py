P = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
Q = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50}

a = {i for i in range(1000)}
for x in range(1000):
    # ((x ∈ A) → (x ∈ P)) ∨ (¬(x ∈ Q) → ¬(x ∈ A))
    res = (x not in a) or (x in P) or (x in Q) or (x not in a)
    if not res:
        a.remove(x)

print(len(a))