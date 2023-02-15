def check(a: int, x: int, y: int, z: int) -> bool:
    return ((z % 115 == 0) or (y % 78 == 0) or (x % 51 == 0)) <= ((x * y * z) % a == 0)


if __name__ == '__main__':
    _max = 0
    for a in range(1, 10):
        if all(check(a, x, y, z) for x in range(1, 500) for y in range(1, 500) for z in range(1, 500)):
            _max = max(_max, a)
    print(_max)
