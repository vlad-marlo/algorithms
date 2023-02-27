from itertools import product

letters = 'ИКНОТ'
c = 1
for i in product(letters, repeat=4):
    print(f'{c=} {"".join(i)}')
    if i[0] == 'О':
        break
    c += 1
