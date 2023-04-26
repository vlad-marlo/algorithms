def algo(n: int) -> int:
    b = bin(n)[2:]
    if n % 3 == 0:
        add = b[len(b)-3:]
        assert len(add)==3
        b += add
    else:
        b += bin(n % 3 * 3)[2:]
    return int(b, 2)


print(algo(12), algo(4))
for i in range(4, 1000):
    if algo(i) > 76:
        print(i)
        break
