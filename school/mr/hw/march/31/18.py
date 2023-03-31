with open('18.csv') as file:
    data = [float(x.replace(',', '.').strip().strip('"').strip("'")) for x in file.readlines()]
    mx = sm = data[0]
    for i in range(1, len(data)):
        if abs(data[i] - data[i-1]) < 8:
            sm += data[i]
        else:
            sm = data[i]
        mx = max(mx, sm)
    print(mx)
