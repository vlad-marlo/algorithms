for x in range(15):
    n = int(f'1{hex(x)[2:]}51', 15) - int(f'3{hex(x)[2:]}2', 15)
    if n % 4 == 0:
        print(x, n // 4)
