def solution(now: int, want: int) -> int:
    if now == want:
        return 1
    if now > want:
        return 0
    return solution(now + 2, want) + solution(now + 4, want) + solution(now + 5, want)


for i in range(31, 1000):
    if solution(31, i) == 1001:
        print(i)