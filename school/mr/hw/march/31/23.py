commands = [lambda x: x + 1, lambda x: x * 2, lambda x: x * 3]


def solution(start, goal, exclude) -> int:
    if start == goal:
        return 1
    if start > goal or start == exclude:
        return 0
    return sum(solution(c(start), goal, exclude) for c in commands)


print(solution(3, 15, 33) * solution(15, 50, 33))

