P = [1, 3, 7]
Q = [1, 2, 4, 5, 6]
A = []


def check(x: int) -> bool:
    return (x in A) or (x not in P) or ((x not in Q) and (x in P))


for i in range(10000):
    if not check(i):
        A.append(i)
print(len(A))
