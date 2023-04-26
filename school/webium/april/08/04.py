commands = [lambda x: x + 1, lambda x: x * 2, lambda x: x * 3]


def solution(start, end, exclude):
    if start > end or start == exclude:
        return 0
    if start == end:
        return 1
    return sum(solution(c(start), end, exclude) for c in commands)


print(solution(3, 15, 33) * solution(15, 50, 33))
