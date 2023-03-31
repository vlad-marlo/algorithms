with open('26_2.txt') as f:
    n = int(f.readline())
    data = [tuple(map(int, f.readline().split())) for _ in range(n)]
    data.sort()
    d = {}
    for k, v in data:
        if d.get(k) is None:
            d[k] = []
        d[k].append(v)

    _row = 0
    _place = 0
    for k, v in d.items():
        if len(v) < 2:
            continue
        for i in range(len(v) - 1):
            if abs(v[i] - v[i + 1]) == 14:
                _place = min(v[i] + 1, v[i+1] + 1)
                _row = k
    print(_row, _place)
