commands = [lambda x: x + 1, lambda x: x * 2, lambda x: x + 3]


def solution(start: int, end: int) -> int:
    if start > end:
        return 0
    if start == end:
        return 1
    return sum(solution(c(start), end) for c in commands)


print(solution(2, 10) * solution(10, 14))
