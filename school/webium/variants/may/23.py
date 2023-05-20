commands = {
    'A': lambda x: x + 2,
    'B': lambda x: x + 3,
    'C': lambda x: x * 2,
}


def solution(start: int, end: int, exclude: int, command: str) -> int:
    if start > end or start == exclude or 'BACA' in command:
        return 0
    if start == end:
        return 1
    return sum(solution(f(start), end, exclude, command + now) for now, f in commands.items())


print(solution(2, 40, 28, ''))
