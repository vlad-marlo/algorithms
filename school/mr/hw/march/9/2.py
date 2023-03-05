def f(n):
    if n <= 0:
        return n
    if n % 2 == 0:
        return f(n//2) + n * 5
    return f(n - 4) - f(n - 6)


print(f(70) + f(56) - f(66) - f(44))