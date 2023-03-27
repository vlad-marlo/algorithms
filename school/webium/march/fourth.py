def algo(num: int) -> int:
    b = bin(num)[2:]
    b = b[:-1] + 2 * b[1]
    return int(b, 2)


assert algo(19) == 36

for i in range(3, 10000):
    if algo(i) > 92:
        print(i, algo(i))
        break
