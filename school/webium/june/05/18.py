import fnmatch


def get_sum_of_divs(num: int) -> int:
    divs = set()
    for div in range(1, int(num ** 0.5) + 1):
        if num % div == 0:
            if div % 2 != 0:
                divs.add(div)
            if (num // div) % 2 != 0:
                divs.add(num // div)
    return sum(divs)


c = 0
for i in range(1484714, 10 ** 7, 217):
    if fnmatch.fnmatch(str(i), '14?4*') and c < 7:
        c += 1
        print(i, get_sum_of_divs(i))
