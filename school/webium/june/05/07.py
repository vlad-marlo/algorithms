def f(s: str) -> str:
    while 'AA' in s or 'BB' in s or 'AB' in s:
        s = s.replace('AA', 'B', 1).replace('BB', 'A', 1).replace('AB', 'BA', 1)
    return s

print(f(52*'AB'))