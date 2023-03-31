for num in range(123456789, 223456789+1):
    if int(num ** 0.5) ** 2 != num:
        continue
    c = 1
    mx = 0
    for div in range(2, int(num ** 0.5)):
        if c > 3:
            break
        if num % div == 0:
            c += 2
            mx = max(mx, num // div)
    else:
        if c == 3:
            print(num, mx)

