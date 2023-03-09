def check(a, x, y):
    return ((108 % x == 0) <= (x % y != 0)) or ((x + y) > 80) or ((a - y) > x)


for A in range(1, 1000):
    for x in range(1, 200):
        for y in range(1, 200):
            if not check(A, x, y):
                break
        else:
            break
    else:
        print(A)
        break
