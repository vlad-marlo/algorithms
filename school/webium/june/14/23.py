from itertools import permutations, product

count = 0
for i in permutations('01234567', r=6):
    s = ''.join(i)
    if i[0] == '0' or len(set(s)) != len(s):
        continue
    if all(''.join(x) not in s for x in permutations('0246', r=2)) and all(''.join(x) not in s for x in permutations('1357', r=2)):
        count += 1
print(count)
