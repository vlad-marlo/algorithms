import fnmatch

for i in range(0, 10**8, 23):
    if fnmatch.fnmatch(str(i), '2*5443?1'):
        print(i, i // 23)
