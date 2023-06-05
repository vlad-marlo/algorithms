data = [int(x) for x in open('13.txt')]
min_8 = min([i for i in range(16, max(data), 8) if i in data])
min_sum = 10 ** 10
ans = 0
count = 0
for i in range(len(data) - 1):
    a, b = data[i:i + 2]
    if a % min_8 == 0 and b % min_8 == 0:
        if a + b < min_sum:
            min_sum = a + b
            ans = max(a, b)
        elif a + b == min_sum:
            print('askdjlfa')
        count += 1
print(count, ans)
