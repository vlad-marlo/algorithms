def algo(num: int) -> int:
    b = bin(num)[2:]
    b += str(b.count('1') % 2) + '0'
    return int(b, 2)


for i in range(1000):
    if algo(i) > 184:
        print(i, algo(i))

