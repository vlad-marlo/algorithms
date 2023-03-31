commands = [lambda x: x + 1, lambda x: x + 2, lambda x: x * 3]

def algo(start, goal):
    if start == goal:
        return 1
    if start > goal:
        return 0
    return sum(algo(i(start), goal) for i in commands)


print(algo(1, 10) * algo(10, 15))
