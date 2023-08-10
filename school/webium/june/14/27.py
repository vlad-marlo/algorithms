from itertools import permutations


count = 0
for raw in permutations('абрикос', r=7):
    word = ''.join(raw)
    if all(a + b not in word for a in 'аио' for b in 'аио') and all(a + b not in word for a in 'бркс' for b in 'бркс'):
        count += 1
        print(word, count)
    
