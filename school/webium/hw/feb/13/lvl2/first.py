def to_system(num: int, base: int) -> str:
    res = []
    while num:
        res.append(str(num % base))
        num //= base
    return ''.join(reversed(res))


def check_num(num: int) -> bool:
    return to_system(num, 6).count('5') == 3


for x in '0123456789ABCDEFG':
    res = int(f'3B8{x}1', 17) + int(f'2{x}9{x}3', 17)
    if check_num(res):
        print(res)
        break
