from itertools import permutations

res = set()
for i in permutations('DIANA', r=5):
    s = ''.join(i)
    if 'DN' not in s and 'ND' not in s:
        res.add(s)
print(len(res))
print(len({s for i in permutations('DIANA', r=5) if 'DN' not in (s := ''.join(i)) and 'ND' not in s}))
print(len(list(filter(
    lambda x: x.count('D') == 1 and x.count('I') == 1 and x.count('A') == 2 and x.count('N') == 1 and not any(
        f'{c}{d}' in x for c in 'DN' for d in 'DN'),
    {f'{a}{b}{c}{d}{e}' for a in 'DIAN' for b in 'DIAN' for c in 'DIAN' for d in 'DIAN' for e in
     'DIAN'}))))
