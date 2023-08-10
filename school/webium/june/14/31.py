for x in range(15):
    n1 = f'99658{hex(x)[2:]}29'
    n2 = f'102{hex(x)[2:]}023'
    print(n1, n2)
    res = int(n1, 15) + int(n2, 15)
    if res % 14 == 0:
        print(x, res // 14)
