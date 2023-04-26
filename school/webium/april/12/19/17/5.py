def solution(s: list[str]) -> int:
    c = sum(1 if i.count('E') < i.count('A') else 0 for i in s)
    return c


print(solution(open('inf_22_10_20_24_3.txt').readlines()))