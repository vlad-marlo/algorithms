def algo(n: int) -> int:
    b = bin(n)[2:]
    b = '1' + b[:len(b)-2] + '01' if b.count('1') % 2 == 0 else '1' + b[2:] + '10'
    return int(b, 2)


assert algo(6) == 13
assert algo(4) == 10
print(max(list(filter(lambda x: x <= 100, [algo(i) for i in range(1000)]))))
