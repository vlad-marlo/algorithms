import itertools

count = 0
basdf = set()
for a in '246':
    for b in '1234560':
        for c in '1234560':
            for d in '1234560':
                for e in '34560':
                    s = a + b + c + d + e
                    if s.count('4') <= 1:
                        basdf.add(s)
print(len(basdf))
res = set()
for i in itertools.product('1234560', repeat=5):
    x = ''.join(i)
    if x[0] in '246' and x.count('4') <= 1 and x[-1] in '345678':
        res.add(x)
print(len(res))
