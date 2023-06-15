def algo(n: int) -> int:
    b = bin(n)[2:]
    b += '11' if n % 2 != 0 else '00'
    return int(b, 2)


print(algo(9), int('100111', 2))
print(max([i for i in range(1000) if algo(i) < 134]))