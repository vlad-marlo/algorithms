steps = [lambda x: x + 1, lambda x: x + 2, lambda x: x * 3]


def sol(now, want, exclude) -> int:
    if now == want:
        return 1
    if now > want or now == exclude:
        return 0
    return sum(sol(f(now), want, exclude) for f in steps)


print(sol(3, 8, 13) * sol(8, 18, 13))
