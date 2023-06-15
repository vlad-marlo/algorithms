def get_count_of_dels(num: int) -> bool:
    res = set()
    for div in range(1, int(num ** 0.5) + 1):
        if num % div == 0:
            res.add(div)
            res.add(num // div)
            if len(res) > 6:
                return False

    if len(res) == 6:
        print(*sorted(res))
    return len(res) == 6


for i in range(312614, 312652):
    get_count_of_dels(i)