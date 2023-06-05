def algo(n: int) -> int:
    b = bin(n)[2:]
    b += str(b.count('1') % 2) + '0'
    return int(b, 2)


print(min([res for i in range(1000) if (res := algo(i)) > 96]))
for i in range(1000):
    if (res := algo(i)) > 96:
        print(res)
        break
