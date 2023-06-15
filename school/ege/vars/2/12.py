def algo(s: str) -> str:
    while '81' in s or '882' in s or '8883' in s:
        if '81' in s:
            s = s.replace('81', '2', 1)
        elif '882' in s:
            s = s.replace('882', '3', 1)
        else:
            s = s.replace('8883', '1', 1)
    return s


print(algo('2' + 99 * '8' + '2'))