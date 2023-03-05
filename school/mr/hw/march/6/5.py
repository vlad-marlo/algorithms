def algo(num):
    b = bin(num)[2:]
    assert int(b, 2) == num
    b += '10' if b.count('1') % 2 else '00'
    return int(b, 2)


assert algo(13) == 54

num = 13
res = algo(num)
while res <= 93:
    num += 1
    res = algo(num)

print(res, algo(num - 1))