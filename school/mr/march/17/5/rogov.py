def algo(n1: int, n2: int) -> int:
    a = n1 // 100 + n2 // 100
    b = n1 // 10 % 10 + n2 // 10 % 10
    c = n1 % 10 + n2 % 10
    return int(f'{c}{a}{b}') // 10 % 1000


status = True
for n1 in reversed(range(100, 1000)):
    for n2 in range(100, 1000):
        if algo(n1, n2) == 2:
            if status:
                print(n1, n2)
                status = not status

print(algo(473, 934))