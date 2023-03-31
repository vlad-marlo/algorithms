a = range(13, 22)
d = []
def check(x):
    return not ((not (x not in a) or (x >= 56)) <= (x < 7)) and (not ((x in a) <= (x >= 56))) == (x in d)


for i in range(10000):
    if not check(i):
        d.append(i)
print(len(d))
