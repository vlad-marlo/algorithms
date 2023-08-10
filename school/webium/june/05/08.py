def algo(s: str) -> str:
    while '777' in s or '73' in s:
        s = s.replace('777', '73', 1) if '777' in s else s.replace('73', '7', 1)
    return s


print(algo(61 * '7'))

a = 3.16
print(a.as_integer_ratio())