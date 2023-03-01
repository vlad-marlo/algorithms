P = [3, 6, 9, 12]
Q = [1, 2, 3, 4, 5, 6]
A = []


def check(x: int) -> bool:
    return not ((x not in A) and (x in P)) or (x not in Q)


for i in range(1500):
    if not check(i):
        A.append(i)
print(len(A))