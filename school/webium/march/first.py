def algo(num: int) -> int:
    s = bin(num)[2:]
    s = s.replace('1', '2').replace('0', '1').replace('2', '0').strip('0') or '0'
    return num - int(s, 2)


assert algo(22) == 13
for i in range(100000, 100000 ** 1000):
    if algo(i) == 979:
        print(i)
        break
