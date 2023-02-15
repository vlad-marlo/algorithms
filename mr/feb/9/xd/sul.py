from collections import Counter

print(Counter(min(open('24.txt').readlines(), key=lambda x: x.count('N'))))
