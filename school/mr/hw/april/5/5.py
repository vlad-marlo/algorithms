def algo(n: int) -> int:
    b = bin(n)[2:]
    b += str(int(b.count('1') % 2 == 0))
    b += str(int(b.count('1') % 2 == 0))
    return int(b, 2)


for i in range(10000):
    if (r := algo(i)) > 54:
        print(r)
        break
