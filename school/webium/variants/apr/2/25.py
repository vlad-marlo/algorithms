import fnmatch

for i in range(273, 10**8, 273):
    if fnmatch.fnmatch(str(i), '12??36*1'):
        print(i, i // 273)