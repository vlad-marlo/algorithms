for n in range(100):
    s = '>' + '0' * 39 + '1' * n + 39 * '2'
    while '>1' in s or '>2' in s or '>0' in s:
        s = s.replace('>1', '22>', 1).replace('>2', '2>', 1).replace('>0', '1>', 1)
    sm = sum(map(int, s.strip('>')))
    if all(sm % i != 0 for i in range(2, int(sm ** 0.5) + 1)):
        print(n, sm)
