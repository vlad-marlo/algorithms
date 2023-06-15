def get_e(num: int) -> int:
    mn, mx = num, 0
    count = 0
    for div in range(2, num):
        for x in range(2, int(div ** 0.5) + 1):
            if div % x == 0:
                break
        else:
            if num % div == 0:
                mn, mx = min(div, mn), max(mx, div)
                count += 1
    return 0 if count == 0 else mx - mn


c = 0
for i in range(22801, 10000000):
    if c == 5:
        break
    if (e := get_e(i)) % 47 == 17:
        print(i, e)
        c += 1
