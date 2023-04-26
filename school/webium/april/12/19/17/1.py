s = open('zadanie24_2_1.txt').read()
strings = s.replace('L', ' ').replace('D', ' ').split()
ans = 0
counter = 0
for i in s:
    if i == 'R':
        counter += 1
        ans = max(ans, counter)
    else:
        counter = 0
print(ans)
