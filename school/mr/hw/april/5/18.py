data = [float(x.strip().strip('"').replace(',', '.')) for x in open('18.csv').read().strip().splitlines()]
mx, now = data[0], data[0]

for i in range(1, len(data)):
    if data[i] >= data[i-1]:
        now = data[i]
        continue
    now += data[i]
    mx = max(mx, now)
print(mx)
