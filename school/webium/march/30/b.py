def algo(n: int) -> int:
    b = bin(n)[2:]
    b += b[1] + b[0]
    return int(b, 2)


for i in range(3, 10000):
    if algo(i) > 74:
        print(i)
        break
