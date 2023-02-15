A = []
P = [1, 2, 3, 4]
Q = [1, 2, 3, 4, 5, 6]


def check(x: int) -> bool:
    return (x not in A) <= ((x not in P) or (x not in Q))


for i in range(1000):
    if not check(i):
        A.append(i)
print(len(A))
