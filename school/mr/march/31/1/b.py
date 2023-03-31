def algo(s: str) -> str:
    while '22222' in s or '9999' in s:
        s = s.replace('22222', '99', 1) if '22222' in s else s.replace('9999', '2', 1)
    return s


print(algo('9' * 135))
