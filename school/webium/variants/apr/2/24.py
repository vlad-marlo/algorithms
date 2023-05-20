s = open('24.txt').read()
for x in 'QRS':
    for y in 'QRS':
        while x + y in s:
            s = s.replace(x + y, x + ' ' + y)
print(len(max(s.split(), key=len)))