def algo(num: int) -> int:
    return int(bin(255 - num), 2)

for i in range(256):
    if algo(i) == 98:
        print(i)