def algo(n: int) -> int:
    b = bin(n)[2:]
    assert len(b[len(b) - 3:]) == 3, b[len(b) - 3:]
    b += b[len(b) - 3:] if n % 3 == 0 else bin((n % 3) * 3)[2:]
    return int(b, 2)


for i in reversed(range(4, 1000)):
    if (res := algo(i)) < 76:
        print(i, res)
        break
