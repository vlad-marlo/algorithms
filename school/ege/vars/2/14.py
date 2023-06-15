num = 16 ** 8 * 4 ** 20 - 4 ** 5 - 64
count = 0
while num:
    count += num % 4 == 3
    num //= 4
print(count)
