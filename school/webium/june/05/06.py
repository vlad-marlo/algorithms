from itertools import permutations

c = 0
data = set()
for i in permutations('СПОРТЛОТО'):
    word = ''.join(i)
    if word[0] == 'О' and word[-1] == 'О':
        data.add(word)
print(len(data))
