commands = [lambda x: x - 2, lambda x: x - 5]


def sol(num: int, to: int) -> int:
    if num == to:
        return 1
    if num < to:
        return 0
    return sol(num - 2, to) + sol(num - 5, to)


print(sol(23, 2))