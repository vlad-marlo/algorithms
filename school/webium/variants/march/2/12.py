def algo(s: str) -> str:
    while '19' in s or '299' in s or '3999' in s:
        s = s.replace('19', '2', 1).replace('299', '3', 1).replace('3999', '1', 1)
    return s


print(algo('3' + '9' * 94))