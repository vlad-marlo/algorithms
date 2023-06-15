from itertools import permutations

count = 0
for raw in permutations('01234567', r=6):
    num = ''.join(raw)
    if all((num[0] != '0', not any(f'{a}{b}' in num for a in '02468' for b in '02468'),
            not any(f'{a}{b}' in num for a in '13579' for b in '13579'), int(num, 8) % 5 == 0)):
        count += 1
        print(num)
print(count)
