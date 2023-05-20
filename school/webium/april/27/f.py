counter = 0
num = 700_000
while counter < 5:
    m = 0
    for div in range(2, int(num ** 0.5) + 1):
        if num % div == 0:
            m = div + num // div
            break
    if m % 10 == 8:
        print(num, m)
        counter += 1
    num += 1
