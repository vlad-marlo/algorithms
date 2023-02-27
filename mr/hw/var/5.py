def algo(num: int) -> int:
    b = bin(num)[2:]
    b += '10' if b.count('1') % 2 else '00'
    return int(b, 2)


x = 0
res = algo(x)
while res <= 55:
    x += 1
    res = algo(x)
print(res, algo(x), algo(x - 1))
