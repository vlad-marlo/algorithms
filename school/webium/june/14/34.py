def to_12(num: int) -> int:
    sm = 0
    while num:
        sm += num % 12
        num //= 12
    return sm


for x in range(8):
    num = int(f'57A{x}9', 16) * int(f'54{x}', 8)
    if to_12(num) == 40:
        print(num)
