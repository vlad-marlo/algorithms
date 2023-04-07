s = open('24.txt').read().strip()
sogl = 'CDF'
gl = 'AO'
combinations = ['AAC', 'AAD', 'AAF', 'AOC', 'AOD', 'AOF', 'OAC', 'OAD', 'OAF', 'OOD', 'OOC', 'OOF']
assert len(set(combinations)) == 12, set(combinations)
for c in combinations:
    s = s.replace(c, 'x')
for i in sogl + gl:
    s = s.replace(i, 'y')
strings = s.strip('y').split('y')
print(len(max(strings, key=len)))
