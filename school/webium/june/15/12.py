def f(start, end, exclude) -> int:
    if start == end:
        return 1
    if start > end or start == exclude:
        return 0
    return f(start + 2, end, exclude) + f(start + 3, end, exclude) + f(start + 5, end, exclude)


print(f(5, 13, 17)*f(13, 25, 17) + f(5,  17, 13) * f(17, 25, 13))