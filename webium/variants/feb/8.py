import itertools

ALPH = sorted('АВТОР')
res = [''.join(x) for x in itertools.product(ALPH, repeat=4)]
res.insert(0, "")
print(res.index('ВАТА'))