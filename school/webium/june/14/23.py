count = 0
for i in range(8 ** 5, 8 ** 6):

    n = oct(i)[2:]
    if len(set(n)) == len(n) and not any(f'{a}{b}' in n for a in '02468' for b in '02468') and not any(f'{a}{b}' in n for a in '13579' for b in '13579'):
        print(n)
        count +=1
    assert len(oct(i)[2:]) == 6

print(count)
