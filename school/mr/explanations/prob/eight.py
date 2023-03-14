import itertools

ans = 0
for i, v in enumerate(itertools.product(sorted('СОЙКА'), repeat=5)):
    s = ''.join(v)
    print(f'{i+1} {s}')
    if s.count('О') <= 1 and 'СС' not in s:
        ans = i + 1
print(ans)
