def f(n: int) -> int:
    res = 1
    for i in range(1, n + 1):
        res *= i
    return int(res)


print(f(2023) / f(2020), 2023 * 2022 * 2021)
