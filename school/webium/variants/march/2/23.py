commands = [lambda x: x + 1, lambda x: x + 3]


def algo(start: int, goal: int) -> int:
    if start > goal:
        return 0
    if start == goal:
        return 1
    return sum(algo(commands[i](start), goal) for i in range(len(commands)))


print(algo(1, 8) * algo(8, 15))
