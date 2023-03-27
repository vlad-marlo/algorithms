from fnmatch import fnmatch

num = 500000
c = 0
while c != 5:
    num += 1
    mx = int(num ** 0.5) + 1
    div_c = 0 
    max_div = 0
    for div in range(2, mx):
        if num % div == 0:
            if max_div == 0:
                max_div = num // div
            div_c += fnmatch(str(div), "*1?3")
            div_c += fnmatch(str(num // div), "*1?3")
            div_c -= div == num // div
    if div_c == 3:
        c += 1
        print(num, max_div)
