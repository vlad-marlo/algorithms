commands = [lambda x: x - 1, lambda x: x - 3, lambda x: x // 3]


def sol(start: int, end: int) -> int:
    if start < end:
        return 0
    if start == end:
        return 1
    return sum(sol(c(start), end) for c in commands)


print(sol(22, 2))