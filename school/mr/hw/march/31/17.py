data = [int(x) for x in open('17.txt')]
mx = 0
count = 0
for i in range(len(data) - 1):
    a = data[i]
    for j in range(i, len(data)):
        b = data[j]
        if (a + b) % 60 == 0 and (a % 40 == 0 or b % 40 == 0):
            count += 1
            mx = max(mx, a + b)
print(count, mx)
