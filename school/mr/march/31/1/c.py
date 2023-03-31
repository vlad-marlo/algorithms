b = range(50, 71)
def check(a, x):
    return (x % a == 0) or ((x in b) <= (x % 16 != 0))
for a in reversed(range(1000)):
    if all(check(a, x) for x in range(1, 1000)):
        print(a)
        break
