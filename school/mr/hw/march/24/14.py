for x in range(21):
    num = int('3200A', 21) + int('16018', 21)
    num += x * 21
    if all((res := num + 2 * y * 21**2) % 12 == 0 for y in range(1, 21, 2)):
        res = num + 2 * 7 * 21 ** 2
        res //= 12
        print(res)
        break
