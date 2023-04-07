for i in range(101_000_000, 102_000_000):
    c = 0

    for div in range(1, int(i ** 0.5) + 1):
        if i % div == 0:
            c += div % 2 == 0
            c += (i // div) % 2 == 0 and (i // div) != div
        if c > 3:
            c += 123
            break
    if c == 3:
        print(i)
