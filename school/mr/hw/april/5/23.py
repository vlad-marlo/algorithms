def solution(start, goal, exclude) -> int:
    if start == goal:
        return 1
    if start > goal or start == exclude:
        return 0
    return solution(start + 1, goal, exclude) + solution(start * 2, goal, exclude)


print(solution(2, 12, 11) * solution(12, 24, 11) + solution(2, 11, 12) * solution(11, 24, 12))
