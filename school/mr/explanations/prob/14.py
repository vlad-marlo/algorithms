num = 2 * 729 ** 1021 - 2 * 243 ** 1022 + 81 ** 1023 - 2 * 27 ** 1024 - 1025
ans = 0
while num:
    ans += (num % 3) == 0
    num //= 3
print(ans)