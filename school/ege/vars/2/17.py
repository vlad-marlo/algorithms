data = [int(x) for x in open('17.txt')]

count = 0
max_sum = 0
for i in range(len(data)-1):
    a = data[i]
    for j in range(i+1, len(data)):
        b = data[j]
        if (a * b) % 26 == 0:
            count += 1
            max_sum = max(max_sum, a + b)
print(count, max_sum)