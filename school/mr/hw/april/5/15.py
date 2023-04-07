P = range(23, 59)
Q = range(1, 40)

def algo(a_start, a_end, x) -> bool:
    x_inA = a_start <= x <= a_end
    return ((x in P) or x_inA) <= ((x in Q) or x_inA)


mn = 10**10
for start in range(100):
    for end in range(start + 1, 102):
        if all(algo(start, end, x) for x in range(1000)):
            mn = min(mn, end + 1 - start)
print(mn)
            
