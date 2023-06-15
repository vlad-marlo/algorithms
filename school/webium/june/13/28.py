# ¬(¬(x ∈ P) → (x ∈ Q)) → ((x ∈ A) →(¬(x ∈ Q)→(x ∈ P)))
# P = [13; 19] и Q = [17; 23].
class Interval:
    def __init__(self, _start: int | float, _end: int | float) -> None:
        self.__start: int | float = _start
        self.__end: int | float = _end

    def __contains__(self, item: int | float) -> bool:
        return self.__start <= item <= self.__end

    def __len__(self) -> int | float:
        return self.__end - self.__start


P = Interval(13, 19)
Q = Interval(17, 23)


def check(a: Interval, x: int | float) -> bool:
    return ((x in P) or (x in Q)) or ((x not in a) or (x in Q) or (x in P))


if __name__ == '__main__':
    mx = 0
    for start in range(100):
        for end in range(start, 100):
            a = Interval(start, end)
            if all(check(a, x) for x in range(100)):
                mx = max(mx, len(a))
    print(mx)
