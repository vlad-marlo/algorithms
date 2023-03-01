def algo(num: int) -> int:
    b_num = bin(num)[2:]
    for _ in range(3):
        b_num += str(sum(map(int, str(num))) % 2)
        num = int(b_num, 2)
    return num


n = 15432090
ans = 0
while True:
    n += 1
    res = algo(n)
    if 123456789 <= res <= 1987654321:
        ans += 1
        print(ans)
    elif res < 123456789:
        continue
    else:
        break
print(f'{ans=}')
