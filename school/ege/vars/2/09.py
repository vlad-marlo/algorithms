with open('107_9.csv') as file:
    data = [list(map(int, x.strip().split(';'))) for x in file.readlines()]
count = 0
for line in data:
    x = sorted(line)
    assert len(x) == 5
    if (x[0] + x[4]) ** 2 > x[1] ** 2 + x[2] ** 2 + x[3] ** 2:
        count += 1
print(count)
