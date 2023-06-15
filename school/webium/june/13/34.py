# ((x ∈ A) → (x ∈ P)) ∧ ((x ∈ Q) → ¬(x ∈ A))
P = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
Q = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50}
A = {i for i in range(1000)}


def check(x) -> bool:
    return ((x in A) <= (x in P)) and ((x in Q) <= (x not in A))


for x in range(1000):
    if not check(x):
        A.remove(x)
print(len(A))
