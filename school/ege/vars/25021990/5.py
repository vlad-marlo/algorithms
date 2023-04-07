def algo(n: int) -> int:
    b = bin(n)[2:]
    b = '10' + b if n % 2 == 0 else '1' + b + '01'
    return int(b, 2)


for i in range(8):
    print(i, algo(i))
