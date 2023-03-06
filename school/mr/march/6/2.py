for a in range(1000):
    if all((x & 51 == 0) or ((x & 41 == 0) <= (x & a == 0)) for x in range(1000)):
        print(a)
        break
