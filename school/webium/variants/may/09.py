class Solution:
    def __init__(self):
        self.__read_data('09.csv')
        self.__ans = 0
        self.__solution()
        print(self.__ans)

    def __read_data(self, filename: str):
        with open(filename) as file:
            self.__data = []
            for line in file.readlines():
                if len(line):
                    self.__data.append(list(map(int, line.replace(';;', '').split(';'))))

    def __solution(self):
        for line in self.__data:
            triples = [x for x in line if x % 3 == 0]
            if len(triples) != 3:
                continue
            self.__ans += max(line) - min(line) <= sum(triples)


Solution()
