with open('09_4.csv') as file:
    data = [list(map(int, x.strip().split(';'))) for x in file.readlines()]
    count = 0
    for line in data:
        dist = []
        for x in line:
            if line.count(x) == 1:
                dist.append(x)
            # elif line.count(x) > 2:
            #     break
        else:
            count += len(dist) == 2 and len(set(line)) == 4 and 2 * sum(dist) < sum(set(line))
    print(count)
