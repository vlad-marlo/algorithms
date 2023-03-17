def algo(num: int) -> int:
    n = bin(num)[2:]
    res = ''
    for i in n:
        res += '0' if i == '1' else '1'
    res = '1' + res
    res += str(res.count('1') % 2)
    return int(res, 2)


for i in range(1, 1000):
    if algo(i) > 180:
        print(i)
        break
