from functools import reduce

P = {1, 3, 4, 9, 11, 13, 15, 17, 19, 21}
Q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
A = set()


def check(x) -> bool:
    return ((x in P) <= (x in A)) or ((x not in A) <= (x not in Q))


for x in range(1000):
    if not check(x):
        A.add(x)
        assert check(x)

res = 1
for i in A:
    res *= i
print(len(A), reduce(lambda a, b: a * b, A), res)
