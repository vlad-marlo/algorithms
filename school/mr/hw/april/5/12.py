def algo(s: str) -> str:
    while '111' in s:
        s = s.replace('11', '2', 1).replace('22', '1', 1)
    return s


print(algo('1'*99))
