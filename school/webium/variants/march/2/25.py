import math

c = 0
for i in range(500000, 1000000**10000):
    if c == 5:
        break
    for div in range(18, int(math.sqrt(i)) + 1, 10):
        if i % div == 0:
            print(i, div)
            c += 1
            break
