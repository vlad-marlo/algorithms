f = open('6.txt')
s = f.readline()
k = m = 0
a = 'DANOV'
for i in range(len(s) - 4):
    b = s[i:i + 5]
    c = 0
    for j in range(len(b)):
        if a[j] == b[j]:
            c += 1
        if c == 4:
            k = 0
        else:
            k += 1
            m = max(k, m)
print(m + 4)
