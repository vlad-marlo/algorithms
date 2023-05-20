def algo(s: str) -> str:
    while '>1' in s or '>2' in s or '>0' in s:
        s = s.replace('>1', '22>', 1).replace('>2', '2>', 1).replace('>0', '1>', 1)
    return s


for i in range(1000000):
    s = '>' + 40 * '0' + i * '1' + 40 * '2'
    if len(str(res := sum(map(int, algo(s).replace('>', ''))))) == 3 and res % 111 == 0:
        print(res, i)
