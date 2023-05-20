from string import punctuation


s = open('10.txt').read().strip().split()
c = 0
for i in s:
    for p in punctuation:
        i = i.replace(p, '')
    if 'час' in i.lower() and i != 'час':
        c += 1
print(c)