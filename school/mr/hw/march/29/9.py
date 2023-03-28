with open('9_6898.csv') as file:
    data = [[int(i) for i in row.strip().split(';')] for row in file.readlines()]
    c = 0
    for row in data:
        row.sort(reverse=True)
        if row[0] < sum(row[1:]) and max(row) + min(row) == sum(row) / 2:
            c += 1
    print(c)
