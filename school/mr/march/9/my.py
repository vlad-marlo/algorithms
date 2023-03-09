B = range(20, 81)
m = 100000
for start in range(100):
    for end in range(start, 101):
        a = range(start, end)
        if all((x in B) <= ((x % 17 == 0) <= (x in a)) for x in range(1000)):
            m = min(len(a) - 1, m)
print(m)
