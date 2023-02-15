num = 7 * 5 ** 1984 - 6 * 25 ** 777 + 5 * 125 ** 333 - 4
ans = 0
while num:
    ans += num % 5
    num //= 5
print(ans)