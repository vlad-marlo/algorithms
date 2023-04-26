commands = [lambda x: x - 1, lambda x: x // 2]


def solution(start, end):
    if start < end:
        return 0
    if start == end:
        return 1
    return sum(solution(c(start), end) for c in commands)


print(solution(89, 30) * solution(30, 7))
