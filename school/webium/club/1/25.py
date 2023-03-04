import fnmatch

for num in range(3332, 10 ** 9, 3333):
    if all([fnmatch.fnmatch(str(num), mask) for mask in ('?[24680]11*', '*4*', '*?7[13579]')]):
        for div in range(2, int(num ** 0.5) + 1):
            if num % div == 0:
                break
        else:
            print(num)
