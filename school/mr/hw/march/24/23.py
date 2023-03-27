commands = [lambda x: x - 4, lambda x: x - sum(map(int, str(x)))]

def find(s: int, res: int) -> int:
    if s < res:
        return 0
    if s == res:
        return 1
    return sum(find(i(s), res) for i in commands)

print(find(36, 14) * find(14, 2))
