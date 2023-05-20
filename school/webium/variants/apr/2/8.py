import itertools

for i, word in enumerate(itertools.product(sorted('АВЛОР'), repeat=5), start=1):
    sword = ''.join(word)
    if sword[0] == 'Л':
        print(i, sword)
        break