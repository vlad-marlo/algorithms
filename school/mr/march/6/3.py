P = list(range(69, 92))
Q = list(range(77, 115))
m = 100000
for i in range(100):
    for j in range(i, 101):
        a = range(i, j)
        if all((x in P) <= (not ((x in P) == (x in Q)) or ((x in Q) <= (x in a))) for x in range(1000)):
            m = min(m, len(a)-1)
print(m)
