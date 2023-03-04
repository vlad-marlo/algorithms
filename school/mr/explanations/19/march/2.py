from functools import lru_cache

commands = [
    lambda x: x + 1,
    lambda x: x * 2,
    lambda x: x + 3,
]


@lru_cache(None)
def solution(num, goal, last):
    if num > goal:
        return 0
    if num == goal:
        return 1
    ans =[]
    for i in range(len(commands)):
        if i != last:
            ans.append(solution(commands[i](num), goal, i))
    return sum(ans)


for n in reversed(range(5001, 45789)):
    for c in range(len(commands)):
        solution(n, 45789, c)

print(solution(5001, 45789, 123123))
