import fnmatch

for num in range(2023, 10**10, 2023):
    if fnmatch.fnmatch(str(num), '32?056*6'):
        print(num, num // 2023)