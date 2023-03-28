def f(n):
    if n > 20:
        return n * n * n + n
    if n % 2 == 0:
        return 3 * f(n + 1) + f(n + 3)
    return f(n + 2) + 2 * f(n + 3)


c = 0
for i in range(1, 1001):
    c += '1' not in str(f(i))
print(c)
