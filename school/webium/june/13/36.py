B = range(50, 71)


def check(a, x, y):
    return (2 * x + y != 150) or (x not in B) or (a > y)


for a in range(1000):
    if all(check(a, x, y) for x in range(1000) for y in range(1000)):
        print(a)
        break
