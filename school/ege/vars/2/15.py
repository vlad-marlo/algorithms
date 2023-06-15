# x&51 = 0 ∨ (x&41 = 0 → x&А = 0)

def check(a, x) -> bool:
    return (x & 51 == 0) or ((x & 41 == 0) <= (x & a == 0))


print(max([a for a in range(1000) if all(check(a, x) for x in range(1000))]))
