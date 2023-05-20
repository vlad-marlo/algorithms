data = [[int(x) for x in i.strip().split(';')] for i in open("9.csv").readlines()]
c = 0
for i in data:
    i.sort()
    if len(set(i)) == len(i) and i.pop(0) * 3 + i.pop(len(i) - 1) * 3 <= sum(i) * 2:
        print(i)
        c += 1
print(c)