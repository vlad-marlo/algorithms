num = 7 * 729 ** 543 - 6 * 81 ** 765 - 5 * 9 ** 987 - 20
ans = 0
while num:
    ans += num % 9 == 8
    num //= 9
print(ans)
