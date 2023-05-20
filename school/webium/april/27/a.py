def get_count(num: int) -> list[int]:
    res = []
    for div in range(2, int(num ** 0.5) + 1):
        if num % div == 0:
            res.append(div)
            if div ** 2 != num:
                res.append(num // div)
    return res


for i in range(210235, 210301):
    divs = get_count(i)
    if len(divs) == 4:
        print(*sorted(divs))
