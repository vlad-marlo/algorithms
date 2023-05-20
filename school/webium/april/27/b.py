num = 600_001
counter = 0
while counter < 5:
    for div in range(17, num, 10):
        if num % div == 0:
            counter += 1
            print(num, div)
            break
    num += 1
