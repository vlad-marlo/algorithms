mx = 0
s = open('24_10_D5.txt').readline()
for i in set(s):
    mx = max(len(max(s.split(i), key=len))+2, mx)
print(mx)
