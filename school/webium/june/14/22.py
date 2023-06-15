from itertools import product


for index, raw in enumerate(product('АКРУ', repeat=5), start=1):
    if index <= 5 or ''.join(raw)== 'УКАРА':
        print(index, ''.join(raw))