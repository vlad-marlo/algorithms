def count_7(num: int) -> int:
    count = 0
    while num:
        count += num % 6 == 5
        num //= 6
    return count


for x in range(17):
    n = hex(x)[2:] if x != 16 else "g"
    n1 = int(f'3B8{n}1', 17) + int(f'2{n}9{n}3', 17)
    if count_7(n1) == 3:
        print(n1)
