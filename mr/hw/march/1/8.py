c = 0
num = 10 ** 9
while c < 5:
    num += 1
    if str(num)[::-1] != str(num):
        continue
    for div in range(2, int(num ** 0.5) + 1):
        if num % div == 0:
            if (num // div) % 7 == 0:
                print(num, num // div)
                c += 1
            break

# output:
# 1001771001 333923667
# 1002002001 334000667
# 1003003001 143286143
# 1004774001 334924667
# 1005005001 335001667
