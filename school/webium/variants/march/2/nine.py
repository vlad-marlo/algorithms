with open('9.csv') as f:
    data = [[int(n) for n in i.split(',')] for i in f.readlines()]
    count = 0
    for line in data:
        if all(sum(line) - i > i for i in line):
            count += 1
    print(count)
