from functools import lru_cache


commands = [
    lambda x: x + int(str(x)[-1]),
    lambda x: x * int(str(abs(x))[0]),
    lambda x: x * 2 + sum(map(int, str(x))),
]


@lru_cache(None)
def solution(num, goal):
    if num == goal:
        return 1
    if num > goal:
        return 0
    return sum([solution(c(num), goal) for c in commands if c(num) > num])


for i in reversed(range(10, 4096)):
    solution(i, 4096)

print(solution(10, 4096))
