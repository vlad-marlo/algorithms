num = 343 ** 515 - 6 * 49 ** 520 + 5 * 49 ** 510 - 3 * 7 ** 530 - 550
count = 0
while num:
    count += num % 7 == 6
    num //= 7
print(count)
