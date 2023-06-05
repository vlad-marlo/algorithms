def algo(n: int) -> int:
    return int(f'10{bin(n)[2:]}' if n % 2 == 0 else f'1{bin(n)[2:]}01', 2)


assert algo(4) == 20, algo(4)
assert algo(5) == 53, algo(5)
for i in range(9):
    print(algo(i))
