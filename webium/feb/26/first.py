for x in range(15):
    res = int(f'12305', 15) + x * 15 + int('10233', 15) + x * 15 ** 3
    if res % 14 == 0:
        print(res // 14, x)
