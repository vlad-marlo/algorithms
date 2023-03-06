for a in reversed(range(1000)):
    if all((x > a) or (y > a) or ((y - 2 * x + 12) != 0) for x in range(1000) for y in range(1000)):
        print(a)
        break


