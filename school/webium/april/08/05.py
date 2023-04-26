commands = [lambda x: x + 1, lambda x: x * 2, lambda x: x * 3]


def sol(start, end, exclude):
    if start > end or start == exclude:
        return 0
    if start == end:
        return 1
    return sum(sol(c(start), end, exclude) for c in commands)


print(sol(2, 15, 11) * sol(15, 25, 11))
