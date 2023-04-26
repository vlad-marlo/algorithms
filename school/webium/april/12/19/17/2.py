from string import ascii_uppercase

s = open('24vlad.txt').read().strip()
res = {l: 0 for l in ascii_uppercase}
for i in range(1, len(s) - 1):
    a, b, c = s[i - 1:i + 2]
    if a == c:
        res[b] += 1
print(*max(res.items(), key=lambda x: x[1]), sep='')
