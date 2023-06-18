from itertools import product

count = 0
for raw in product('0123456', repeat=5):
    word = ''.join(raw)
    if int(word[0]) % 2 == 0 and word[0] != '0' and word.count('4') <= 1 and word[-1] in '3456':
        count += 1
print(count)
