ans = 100000000000000000000
for x in range(9):
    for y in range(9):
        n1 = int('88040', 9) + x * 9 ** 2 + y
        n2 = int('70440', 11) + x * 11 ** 3 + y
        if (n1 + n2) % 61 == 0:
            ans = min(ans, n1 + n2)
print(ans // 61)
