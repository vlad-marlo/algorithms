import fnmatch


def get_count_of_divs(num: int) -> int:
    divs = set()
    for div in range(1, int(num ** 0.5) + 1):
        if num % div == 0:
            divs.add(div)
            divs.add(num // div)
    return len(divs)


def is_saldkjf(num: int) -> bool:
    while num != 1:
        if num % 2 != 0:
            return False
        num //= 2
    return True


for i in range(200):
    assert is_saldkjf(2 ** i)
    assert not is_saldkjf((2 ** i) + 5), 2 ** i + 5

for i in range(2031, 10 ** 9, 2031):
    if fnmatch.fnmatch(str(i), '*31*65?') and i % 31 == 0 and is_saldkjf(get_count_of_divs(i)):
        print(i, i // 2031)
