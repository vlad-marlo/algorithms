commands = [
    lambda x: x - 2,
    lambda x: x - (x // 2)
]

def algo(s, e) -> int:
    if s < e:
        return 0
    if s == e:
        return 1
    return algo(s - 2, e) + algo(s - (s//2), e)


print(algo(40, 10) * algo(10, 2))
