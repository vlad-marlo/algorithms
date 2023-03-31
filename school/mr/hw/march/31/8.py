from itertools import permutations


count = 0

for i in permutations('ольга'):
    s = ''.join(i)
    if 'ь' == s[0]:
        continue
    if 'оь' not in s and 'аь' not in s:
        count += 1
print(count)

