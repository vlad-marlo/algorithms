def check(a, x, y):
    return (x > 7) or (y > 4) or (x ** 2 + 3 * y < a)


for a in range(1, 1000):
    if all(check(a, x, y) for x in range(1000) for y in range(1000)):
        print(a)
        break
