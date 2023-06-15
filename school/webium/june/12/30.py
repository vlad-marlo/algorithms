data = [list(sorted(map(int, s.strip().split(';')))) for s in open('30.csv').readlines()]
count = 0
for i in data:
    count += len(i) == len(set(i)) and i[0] + i[-1] < sum(i) - (i[0] + i[-1])
print(count)
