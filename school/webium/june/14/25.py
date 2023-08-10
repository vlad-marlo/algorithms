from itertools import product

count = 0
for raw in product(set('самокат'), repeat=7):
    word = ''.join(raw)
    count += any(x + 'сам' + x in word for x in 'ао')
print(count)

