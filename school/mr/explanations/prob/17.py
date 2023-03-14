with open('17_6752.txt') as f:
    data = [int(x) for x in f.readlines()]
    triples = len([x for x in data if abs(x) % 3 == 0])
    count = 0
    m = 0
    for i in range(len(data) - 1):
        a, b = data[i:i+2]
        if (a < 0 or b < 0) and (a + b < triples):
            m = max(m, a + b)
            count += 1
    print(count, m)

