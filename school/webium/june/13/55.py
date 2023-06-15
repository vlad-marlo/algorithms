class Interval:
    def __init__(self, _start: int, _end: int) -> None:
        self.__start = _start
        self.__end = _end

    def __contains__(self, item):
        return self.__start <= item <= self.__end

    def __len__(self) -> int:
        return self.__end - self.__start


# ((x ∈ A) ∧ (x ∉ Q)) → ((x ∈ P) ∨ (x ∈ Q))
# P = [15, 33] и Q = [45, 68]
P = Interval(15, 33)
Q = Interval(45, 68)


def check(a: Interval, x: int) -> bool:
    return ((x in a) and (x not in Q)) <= ((x in P) or (x in Q))


mx = 0
for start in range(100):
    for end in range(start, 100):
        a = Interval(start, end)
        if all(check(a, x) for x in range(1000)):
            mx = max(mx, len(a))
print(mx)
