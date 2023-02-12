with open('17.txt') as f:
    data = list(map(int, f.readlines()))
    _max_3 = max(filter(lambda x: str(x)[-1] == '3', data)) ** 2
    _count = 0
    _max = 0
    for i in range(len(data) - 1):
        a, b = data[i], data[i + 1]
        if len(list(filter(lambda x: str(x)[-1] == '3', [a, b]))) == 1 and a ** 2 + b ** 2 >= _max_3:
            _count += 1
            _max = max(_max, a ** 2 + b ** 2)
    print(_count, _max)
