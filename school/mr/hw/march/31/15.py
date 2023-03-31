def check(x, y, a) -> bool:
    return ((x in a) <= (x ** 2 <= 81)) and ((y ** 2 <= 36) <= (y in a))


mx = 0
for start in range(100):
    for end in range(start, 101):
        a = range(start, end)
        if all(check(x, y, a) for x in range(100) for y in range(100)):
            mx = max(len(a), mx)
print(mx)
