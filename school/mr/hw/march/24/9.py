def prog(s: list[int]) -> bool:
    s.sort()
    n = s[1] - s[0]
    for i in range(len(s) - 1):
        a, b = s[i:i+2]
        if abs(a - b) != n:
            return False
    return True

with open('9_5627.csv') as f:
    data = [s for x in f.readlines() if len((s := list(map(int, x.strip().split(',')))) ) != len(set(s)) or prog(s)]
    print(len(data))
