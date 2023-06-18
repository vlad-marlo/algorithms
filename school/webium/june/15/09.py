def f(s, end,):
    if s < end:
        return 0
    if s == end:
        return 1
    return f(s - 1, end) + f(s // 2, end)


print(f(30, 9) * f(9, 1))