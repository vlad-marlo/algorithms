for num in range(45_000_000, 50_000_001):
    count_of_odd_divs = 0 if int(num ** 0.5) ** 2 != num else -1
    for div in range(1, int(num ** 0.5) + 1):
        if num % div == 0:
            count_of_odd_divs += (div % 2) + ((num // div) % 2)
        if count_of_odd_divs > 5:
            break
    else:
        if count_of_odd_divs == 5:
            print(num)
