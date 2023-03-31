s = open('24.txt').read().strip()

print(len([i for i in s.replace('E', 'E E').split() if 'F' not in i and len(i) >= 12 and i.count('E') == 2]))
