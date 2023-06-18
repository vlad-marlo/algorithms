def algo(n: int) -> int:
    return 255-n


for i in range(1, 256):
    if algo(i) == 98:
        print(i)