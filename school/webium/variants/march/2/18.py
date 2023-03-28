with open('18.csv') as file:
    data = [float(x.strip().strip('"').strip("'").replace(',', '.')) for x in file.readlines()]
    mx = 0
    loc = data[0]
    for i in range(1, len(data)):
        if data[i - 1] > data[i]:
            loc += data[i]
            mx = max(mx, loc)
        else:
            loc = 0
    print(len(data), mx)