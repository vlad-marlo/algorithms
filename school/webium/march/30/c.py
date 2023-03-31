def f(n):
    b = bin(n)[2:]
    b = b[:-1]
    b += '10' if n % 2 != 0 else '01'
    return int(b, 2)


for i in range(1, 1999999):
    if f(i) == 2018:
        print(i)
        break
