for x in range(15):
    n1 = int('97968013', 15) + x * 15 ** 2
    n2 = int('70213', 15) + x * 15 ** 3
    if (res := n1 + n2) % 14 == 0:
        print(res // 14, x)
        break
