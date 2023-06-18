def solution(start, end, exclude) -> int:
    if start > end or start == exclude:
        return 0
    if start == end:
        return 1
    return solution(start + 1, end, exclude) + solution(start + 2, end, exclude) + solution(start * 3, end, exclude)


print(solution(4, 10, 12) * solution(10, 22, 20))