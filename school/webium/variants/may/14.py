def get_sum(num: int, base: int) -> int:
    sm = 0
    while num:
        sm += num % base
        num //= base
    return sm

for x in range(16):
    n1 = int('B7A09', 16) + x * 16
    n2 = int('540ED', 16) + x * 16 ** 2
    s = n1 + n2
    if get_sum(s, 6) == 25:
        print(x, s)