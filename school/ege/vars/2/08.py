res = set()
for a in 'XZ':
    for b in 'XZ':
        for c in 'ABCDE':
            for d in 'ABCDE':
                res.add(f'{a}{b}{c}{d}')
print(len(res))
