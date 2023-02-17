with open('9.csv') as f:
    data = f.readlines()
    triples = [list(map(int, x.strip('\n').split(','))) for x in data]
    __counter = 0
    for triple in triples:
        a, b, c, d = sorted(triple)
        __counter += not (a < (b + c + d) and b < (a + c + d) and c < (a + b + d) and d < (a + b + c))
    print(__counter)
