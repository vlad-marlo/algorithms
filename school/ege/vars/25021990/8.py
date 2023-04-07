from itertools import product


alp = 'АЙКОС'

for i, word in enumerate(product(alp, repeat=5), start=1):
    word = ''.join(word)
    if i <= 6:
        print(i, word)
