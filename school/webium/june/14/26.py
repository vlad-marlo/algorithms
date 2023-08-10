from itertools import product

count = 0
for raw in product('елй', repeat=6):
    word = ''.join(raw)
    count += all(['й' not in (word[0], word[-1]), word.count('й') <= 1, not any(x in word for x in ('ей', 'йе'))])
print(count)
