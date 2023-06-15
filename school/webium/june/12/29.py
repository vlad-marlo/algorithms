data = [list(sorted(map(int, s.strip().split(';')))) for s in open('29.csv').readlines()]

count = 0
for i in data:
    if len(set(i)) == len(i) and 3 * (i[0] + i[-1]) >= 2 * (i[1] + i[2] + i[3]):
        count += 1
print(count)