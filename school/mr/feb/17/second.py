# https://inf-ege.sdamgia.ru/problem?id=47022

def m(n: int) -> bool:
    c = 0
    for div in range(2, n//2 + 1):
        c += n % div == 0
        if c == 5:
            print(n // div)
            return True
    return False


n = 300_000_001
c = 0
while c < 5:
    c += m(n)
    n += 1
