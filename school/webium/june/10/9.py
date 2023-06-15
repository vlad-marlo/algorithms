data = [list(sorted(map(int, x.strip().split(';')))) for x in open('9_2.csv').readlines()]

count = 0
print(data)
for line in data:
    a, b, c, d = line
    count += sum(line[1:]) > 6 * line[0] and a * d > c * b
print(count)
