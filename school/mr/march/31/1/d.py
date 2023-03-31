x = [int(i) for i in open('17.txt')]
count, mx = 0, 0
max_triple = max(i for i in x if abs(i) % 10 == 3)
for i in range(len(x) - 1):
    a, b = x[i:i+2]
    if (abs(a) % 10 == 3) != (abs(b) % 10 == 3) and (a ** 2 + b ** 2) >= max_triple ** 2:
        count+= 1
        mx = max(mx, a ** 2 + b ** 2)

print(count, mx)
