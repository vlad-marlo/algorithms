from itertools import permutations

count = 0
for raw in permutations('компьютер', r=9):
    word = ''.join(raw)
    if ''.join(sorted(word[:4])) == word[:4] and word[-2] == 'е':
        count += 1
        print(word, count)
print(count)
