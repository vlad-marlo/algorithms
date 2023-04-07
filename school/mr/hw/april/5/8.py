from itertools import product

alphabet = sorted('ТИМОФЕЙ')

data = set()
for i in product(alphabet, repeat=5):
    if i.count('Т') >= 1 and i.count('Й') <= 1:
        data.add(''.join(i))
print(len(data))
