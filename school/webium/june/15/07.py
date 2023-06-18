def solution(start, end, exclude) -> int:
    if start > end or start == exclude:
        return 0
    if start == end:
        return 1
    return solution(start + 1, end, exclude) + solution(start + 2, end, exclude) + solution(start * 2, end, exclude)


print(solution(2, 9, 12) * solution(9, 17, 12))