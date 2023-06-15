from itertools import product

for index, raw in enumerate(product(sorted('ВЕНОК'), repeat=5), start=1):
    word = ''.join(raw)
    if word.count('Н') == word.count('К') == 2 or index <= 6:
        print(word, index)