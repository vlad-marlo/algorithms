class Interval:
    def __init__(self, start: int, end: int) -> None:
        self.__start: int = start
        self.__end: int = end

    def __contains__(self, item: int) -> bool:
        return self.__start <= item <= self.__end

    def __len__(self) -> int:
        return self.__end - self.__start


# ((x ∈ A) → (x ∈ P)) V (x ∈ Q)
P = Interval(43, 49)
Q = Interval(44, 53)


def check(a: Interval, x: int) -> bool:
    return (x not in a) or (x in P) or (x in Q)


ans = 0
for start in range(100):
    for end in range(start, 101):
        A = Interval(start, end)
        if all(check(A, x) for x in range(1000)):
            ans = max(ans, len(A))
print(ans)
