def solution(now, want) -> int:
    if now > want:
        return 0
    if now == want:
        return 1
    return solution(now + 1, want) + solution(now * 2, want) + solution(now * 3, want)


print(solution(1, 13))