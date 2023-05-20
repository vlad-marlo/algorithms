c = 1
for num in range(194493, 196501, 100):
    for div in range(2, int(num ** 0.5) + 1):
        if num % div == 0:
            break
    else:
        print(c, num)
        c += 1
