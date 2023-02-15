for x in range(15):
    _num_1 = int('13101', 15) + (x * 15)
    _num_2 = int('1303', 17) + (x * 17)
    res = _num_2 + _num_1
    if res % 11 == 0:
        print(res // 11)
