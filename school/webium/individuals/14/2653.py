class Solution:
    def __init__(self, filename: str) -> None:
        self.__max = 0
        self.__count = 0

        self.__read_data(filename)
        self.__solution()

    def __read_data(self, filename: str) -> None:
        with open(filename) as file:
            self.__data = list(map(int, file.readlines()[1:]))
            return

    def __solution(self) -> None:
        self.__data.sort()
        weights = [False for _ in range(sum(self.__data) + 1)]
        s = 0
        for x in self.__data:
            w = weights[:]
            for i in range(s + 1):
                if weights[i]:
                    w[i + x] = True
            w[x] = True
            weights = w
            s += x
        for i in range(1, sum(self.__data) + 1):
            if not weights[i]:
                self.__count += 1
                self.__max = i

    def __str__(self) -> str:
        return f'{self.__count} {self.__max}'


print(Solution('26_2653.txt'))
