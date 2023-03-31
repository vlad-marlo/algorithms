def algo(s: str) -> str:
    while '>1' in s or '>2' in s or '>3' in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>3' in s:
            s = s.replace('>3', '1>', 1)
    return s


res = algo('>' + 10 * '1' + 20 * '2' + 30 * '3')
print(res.count('2') * 2 + res.count('1') + res.count('3') * 3)
print(sum(int(i) for i in res if i != '>'))
