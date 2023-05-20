import fnmatch

for num in range(7424, 10 ** 8, 10_000):
    if fnmatch.fnmatch(str(num), '*15*7424') and sum([num % div == 0 for div in (111, 113, 127)]) == 1:
        if num % 111 == 0:
            print(num, num // 111)
        elif num % 113 == 0:
            print(num, num // 113)
        else:
            print(num, num // 127)
