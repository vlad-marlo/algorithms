print(len(max(open('24.txt').read().strip().replace('CFE', 'x').replace('FCE', 'x').replace('C', ' ').replace('D', ' ').replace('E', ' ').replace('F', ' ').split(), key=len)))

