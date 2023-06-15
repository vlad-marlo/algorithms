s = open('24.txt').read()
s = s.replace('AA', 'A A').replace('BB', 'B B').replace('AC', 'A C').replace('BC', 'B C').replace('CA', 'C A').replace(
    'CB', 'C B')
print(max(s.split(), key=len))
