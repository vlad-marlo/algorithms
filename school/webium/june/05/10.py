for x in range(111):
    n1 = x * 111 ** 3 + 3 * 111 ** 2 + 2 * 111 + 1
    n2 = 211 ** 3 + 7 * 211 ** 2 + x * 211 + 4
    if (res := n1 + n2) % 111 == 0:
        print(res // 111, x)