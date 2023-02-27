def phd_definer(__num: int) -> int:
    __c = 0
    _ans = 1
    for divider in range(2, __num // 2):
        if __num % divider == 0:
            _ans *= divider
            __c += 1
            if __c == 5:
                return _ans
    return -1


num = 200_000_000
count = 0
while count < 5:
    num += 1
    res = phd_definer(num)
    if 0 < res < num:
        count += 1
        print(res)
