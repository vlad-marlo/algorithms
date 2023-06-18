def f(n):
    if n >= 2025:
        return n
    return n + 3  + f(n + 3)


print(f(2018)-f(2022))