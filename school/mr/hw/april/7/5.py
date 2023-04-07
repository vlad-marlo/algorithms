def algo(n: int) -> int:
    b = bin(n)[2:]
    for _ in range(2):
        if b.count('1') % 2 == 0:
            b = '11' + b[2:] + '00'
        else:
            b = '10' + b[2:] + '11'
    return int(b, 2)


print(algo(6), algo(4))
print(max(algo(i) for i in range(2, 100)))
