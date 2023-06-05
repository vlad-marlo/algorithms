from math import gcd

data = [int(x) for x in open('14.txt')]
count, max_diff = 0, 0
for i in range(len(data) - 1):
    a, b = data[i:i + 2]
    if gcd(a, b) > 100 and a % 2 == 0 and b % 2 == 0 and 0 not in (a, b):
        count += 1
        max_diff = max(max_diff, abs(a - b))

print(count, max_diff)
