n = 3 * 256 ** 320 - 2 * 64 ** 290 + 4 ** 250 - 1023
count = 0
while n:
    count += (n % 4) > 0
    n //=4
print(count)