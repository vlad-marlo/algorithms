def algo(n: int) -> int:
    return int(bin(n)[2:][::-1], 2)


for i in range(1000, 199999):
    if (b := algo(i)) == 29:
        print(i)
