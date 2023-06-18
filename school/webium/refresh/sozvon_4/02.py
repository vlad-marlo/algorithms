import fnmatch


def check(i: int) -> tuple[int, int]:
    _sm, _count = 0, 0
    for div in range(1, int(i ** 0.5) + 1):
        if i % div == 0:
            _count += 2
            _sm += div + (i // div)
    return _sm, _count


for i in range(53, 10 ** 7, 53):
    sm, count = check(i)
    if fnmatch.fnmatch(str(i), '*2?2*') and str(i) == str(i)[::-1] and count > 30:
        print(i, sm)
