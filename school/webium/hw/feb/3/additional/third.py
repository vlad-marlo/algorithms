from functools import lru_cache


@lru_cache(None)
def bin_del(n: int, m: int) -> bool:
    return bin(n)[2:].count('1') % m == 0


@lru_cache(None)
def check_count_of_dividers_more_than(n: int, m: int) -> bool:
    dividers_n = [div for div in range(1, n) if n % div == 0]
    return len(dividers_n) > m


@lru_cache(None)
def check(a: int, x: int) -> bool:
    return (bin_del(x, 4) <= check_count_of_dividers_more_than(a, 22)) and (
            bin_del(a, 2) <= check_count_of_dividers_more_than(x, 69))


def solution() -> int:
    a = 0
    while True:
        a += 1
        if all(check(a, x) for x in range(1000)):
            return a


if __name__ == '__main__':
    print(solution())
