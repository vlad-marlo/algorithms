def solution(start: int, end: int, exclude: int, commands) -> int:
    if start == exclude or start > end:
        return 0
    if start == end:
        return 1
    return sum(solution(command(start), end, exclude, commands) for command in commands if command(start) != start)


COMMANDS = [
    lambda x: x + 5,
    lambda x: int(f'{first + 1}{str(x)[1:]}') if (first := int(str(x)[0])) != 9 else x
]

print(solution(30, 60, 35, commands=COMMANDS))
