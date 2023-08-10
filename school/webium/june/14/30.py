num = 3 * 625 ** 173 + 4 * 125 ** 180 + 3 * 25 ** 157 + 2 * 5 ** 155 + 156
count = 0
while num:
    count += num % 25 == 0
    num //= 25
print(count)
