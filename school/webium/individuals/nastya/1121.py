f = open('27_A_1233.txt')
n = int(f.readline())
k = 101
data = [[] for _ in range(n)]
for line in range(n):
    data[line] = [int(x) for x in f.readline().split()]

min_diff = 10 ** 10
mx = 0
now = 0
for line in data:
    a, b, c = sorted(line)
    now += c
    if (c - b) % k != 0:
        min_diff = min(c - b, min_diff)
    if (c - a) % k != 0:
        min_diff = min(c - a, min_diff)
if now % k == 0:
    now -= min_diff
print(now)
