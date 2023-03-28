with open('24.txt') as f:
    s = f.readline().strip().replace('EBCF', 'xxxx').replace('EBC', 'yyy').replace('EB', 'yy').replace('E', 'y')
    for i in 'ABCDEF':
        s = s.replace(i, ' ')
    print(len(max(s.strip().split(), key=len)))