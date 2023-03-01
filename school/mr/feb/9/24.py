with open('24.txt') as f:
    data = f.readline()
    for i in ['CA', 'CO', 'DA', 'DO', 'FA', 'FO']:
        data = data.replace(i, 'x')
    _max = 0
    _count = 0
    for i in data:
        if i == 'x':
            _count += 1
        else:
            _max = max(_max, _count)
            _count = 0
    print(_max)
