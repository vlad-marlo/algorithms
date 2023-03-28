import itertools

x = [i for i in itertools.product('балкон', repeat=4) if 'б' in i]
print(x, len(x), sep='\n')
