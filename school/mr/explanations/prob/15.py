def check(a, x, y):
    return (x + y <= 32) or (y <= x + 4) or (y >= a)


for a in reversed(range(1000)):
    if all(check(a, x, y) for x in range(1000) for y in range(1000)):
        print(a)
        break