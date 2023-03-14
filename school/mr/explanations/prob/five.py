def algo(n: int) -> int:
    b = bin(n)[2:]
    if n % 2 == 0:
        b = '10' + b
    else:
        b = '1' + b + '01'
    return int(b, 2)


assert algo(4) == 20
assert algo(5) == 53

for i in range(9):
    print(i, algo(i))
