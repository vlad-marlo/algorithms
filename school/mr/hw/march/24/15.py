for a in range(1, 1000):
    if all(((x % 3 == 0) <= (x % 17 != 0)) or not (a < 190 - x) for x in range(1, 1000)):
        print(a)
        break
