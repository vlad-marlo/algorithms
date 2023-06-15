class Interval:
    def __init__(self, _start: int, _end: int) -> None:
        self.__start = _start
        self.__end = _end

    def __contains__(self, item: int | float) -> bool:
        return self.__start <= item <= self.__end

    def __len__(self) -> int:
        return self.__end - self.__start


P = Interval(12, 26)
Q = Interval(30, 53)
mx = 0


def check(a: Interval, x: int | float) -> bool:
    return (x not in a) or (x in P) or (x in Q)


for start in range(100):
    for end in range(start, 100 + 1):
        a = Interval(start, end)
        if all(check(a, x) for x in range(100)):
            mx = max(mx, len(a))
print(mx)
