def algo(n: int) -> int:
    b = bin(n)[2:]
    b = '10' + b[2:] + '0' if b.count('1') % 2 == 0 else '11' + b[2:] + '1'
    return int(b, 2)


assert algo(6) == 8, f'want: 8; got: {algo(6)}'
assert algo(4) == 13, f'want: 13; got: {algo(4)}'

for i in range(4, 10000000):
    if algo(i) >= 60:
        print(i, algo(i))
        break
