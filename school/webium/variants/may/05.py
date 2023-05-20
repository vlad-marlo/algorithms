def algo(n: int) -> int:
    b = bin(n)[2:]
    if b[-1] == '0':
        b = b[:-1] + '1'
    else:
        b = b[:-1] + '0'
    b += str(sum(map(int, b)) % 2)
    return int(b, 2)


mn = 100
ans = 10
for i in range(1, 1000):
    if (res := algo(i)) > 78:
        if res < mn:
            mn = res
            ans = i
print(algo(13), mn, ans)
