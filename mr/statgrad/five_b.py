def algo(num: int) -> int:
    b_num = bin(num)[2:]
    for _ in range(3):
        b_num += str(sum(map(int, str(num))) % 2)
        num = int(b_num, 2)
    return num


n = 15432099
ans = 0
to_min = 0
while True:
    n += 1
    res = algo(n)
    print(res, n)
    if res - 123456789 <= 8:
        to_min = n
        break

n = 1987654321 // 8 + 1000
ans = 0
to_max = 0
while True:
    n -= 1
    res = algo(n)
    if res + 8 <= 1987654321:
        to_max = n
        break
print(abs(to_min - to_max))
