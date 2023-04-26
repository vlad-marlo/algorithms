from itertools import product
alphabet = sorted('АКЛМНЯ')
for i, word in enumerate(product(alphabet, repeat=5), start=1):
    word = ''.join(word)
    if i <= 7:
        print(i, word)
    if word.startswith('КМ'):
        print(i, word)
        break
