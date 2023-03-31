def algo(num: int) -> int:
    return int((b := bin(num)[2:]) + b[-2] + b[1], 2)


print(algo(13))

print(min([i for i in range(2, 1000) if algo(i) > 150]))
