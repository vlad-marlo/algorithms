def algo(n: int) -> int:
    b = bin(n)[2:]
    if n % 3 == 0:
        assert len(b[len(b) - 3:]) == 3
        b += b[len(b) - 3:]
    else:
        b += bin((n % 3) * 3)[2:]
    return int(b, 2)


for i in reversed(range(1000)):
    if algo(i) < 100:
        print(i, algo(i))
        break