with open('9.csv') as f:
    data = f.readlines()
    triples = [list(map(int, x.strip('\n').split(','))) for x in data]
    __counter = 0
    for triple in triples:
        a, b, c = sorted(triple)
        __counter += (c ** 2) == (a ** 2) + (b ** 2)
    print(triples)
    print(__counter)
