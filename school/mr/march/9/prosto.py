for a in range(4_000_000):
    if all(((680 * y + 256 * x) < a) or ((5 * x + 3 * y) > 11_111) for x in range(2224) for y in range(3705)):
        print(a)
        break
