def algo(num: int) -> int:
    b = bin(num)[2:]
    for _ in range(3):
        b += '1' if (ones := b.count('1')) < (zeros := b.count('0')) else '0' if zeros < ones else b[-1]
    return int(b, 2)


assert algo(19) == 153
for i in range(100, 100000):
    if algo(i) % 4 == 0:
        print(i)
        break
