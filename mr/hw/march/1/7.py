import fnmatch

for num in range(0, 10 ** 7, 53):
    if str(num)[::-1] == str(num) and fnmatch.fnmatch(str(num), '*2?2*'):
        __count = 0
        __sum = 0
        for div in range(2, int(num ** 0.5) + 1):
            if num % div == 0:
                __sum += div + (num // div)
                __count += 2
            if num == div ** 2:
                __count -= 1
                __sum -= div
        if __count > 30:
            print(num, __sum)
# output:
# 212212 295819
# 2527252 3061099
# 4282824 9506615
# 8125218 11470301
# 8824288 11084215
