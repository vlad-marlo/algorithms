def algo(n: int) -> int:
    b = bin(n)[2:]
    b = b[::-1]
    return int(b, 2)


assert algo(58) == 23, algo(58)
for i in reversed(range(101)):
    if algo(i) == 13:
        print(i)
        break