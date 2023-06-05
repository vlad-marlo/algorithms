from itertools import product

for i, word in enumerate(product('АВОРТ', repeat=6), start=1):
    word = ''.join(word)
    if word == 'ВОРОТА':
        print(i)
        
