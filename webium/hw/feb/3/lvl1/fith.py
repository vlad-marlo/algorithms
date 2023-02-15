P = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
Q = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
x = 1
a = []
r = (x not in a) or (x in P) or (x in Q)
for n in range(100):
    if (n in P) or (n in Q):
        a.append(n)
print(len(a))
if all((x not in a) or (x in P) or (x in Q) for x in range(1000)):
    print(len(a))
