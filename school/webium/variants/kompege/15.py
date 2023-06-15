class Interval:
    def __init__(self, _start, _end):
        self.__start = _start
        self.__end = _end

    def __contains__(self, item):
        return self.__start <= item <= self.__end

    def __len__(self):
        return self.__end - self.__start


P = Interval(40, 45)
Q = Interval(10, 33)


def check(a: Interval, x: int) -> bool:
    return (x not in Q) or (x in a) or (x in P)


mn = 10 ** 10
for start in range(1000):
    for end in range(start, 1000):
        A = Interval(start, end)
        if all(check(A, x) for x in range(1000)):
            mn = min(len(A), mn)
print(mn)
