from itertools import product


alphabet = sorted('БАРШ')

mx = 0
for i, word in enumerate(product(alphabet, repeat=5), start=1):
    if len(set(word)) == 4 and word.count('А') == 2:
        print(i, ''.join(word))
