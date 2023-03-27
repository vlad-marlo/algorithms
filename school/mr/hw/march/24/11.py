def is_prime(num: int) -> bool:
    for div in range(2, int(num ** 0.5) + 1):
        if num % div == 0:
            return False
    return True


def replace(s: str) -> str:
    while '>1' in s or '>3' in s or '>2' in s:
        if '>1' in s:
            s = s.replace('>1', '1>', 1)
        if '>2' in s:
            s = s.replace('>2', '>1', 1)
        if '>3' in s:
            s = s.replace('>3', '>1', 1)
    return s


for i in range(32, 1000):
    if is_prime(i):
        print(i - 32)
        break
