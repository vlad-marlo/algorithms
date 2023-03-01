def check(a: int, x: int) -> bool:
    return ((x & 35 != 0) or (x & 22 != 0)) <= ((x & 15 == 0) <= (x & a != 0))


if __name__ == '__main__':
    for a in range(10000):
        if all(check(a, x) for x in range(1000)):
            print(a)
            break
