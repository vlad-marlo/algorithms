from itertools import product

c = set()
for i in product('qwerty', repeat=7):
    if 'qwerty' not in (res := ''.join(i)) and all(res.count(i) <= 2 for i in res):
        c.add(res)
print(len(c))
