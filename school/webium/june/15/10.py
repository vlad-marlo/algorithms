def f(start, end, exclude):
    if start == exclude or start > end:
        return 0
    if start == end:
        return 1
    return f(start + 3, end, exclude) + f(start * 2, end, exclude)


print(f(1, 16, 32) * f(16, 41, 32))
