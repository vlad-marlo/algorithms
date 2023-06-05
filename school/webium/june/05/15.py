def solution(now: int, want: int, exclude: int) -> int:
    if now == exclude or now > want:
        return 0
    if now == want:
        return 1
    return solution(now + 2, want, exclude) + solution(now + 3, want, exclude) + solution(now + 5, want, exclude)


print(solution(5, 13, 17) * solution(13, 25, 17) + solution(5, 17, 13) * solution(17, 25, 13))
