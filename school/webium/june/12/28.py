data = [list(sorted(map(int, s.strip().split(';')))) for s in open('28.csv').readlines()]
count = 0
for i in data:
    if len(set(i)) == 1:
        count += 1
print(count)