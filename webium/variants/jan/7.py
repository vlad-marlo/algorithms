I = 80 * 2 ** 23
V = 2 ** 25
COMPRESS_TIME = 15 + 3


def first(i: int) -> int:
    i *= 0.35
    return i // V + COMPRESS_TIME


def second(i: int) -> int:
    return i // V


print(first(I), second(I), abs(first(I) - second(I)))