class Solution:
    def __init__(self):
        self.__lines: list[str] = []
        self.__read_data()
        self.__solution()

    def __read_data(self):
        with open('24.txt') as file:
            self.__lines = file.readlines()

    def __check_line(self, i: int) -> bool:
        line = self.__lines[i]
        letters = 'QWERTY'
        for letter in letters:
            if letter not in line:
                return False
            line = line[line.index(letter):]
        return True

    def __solution(self):
        print(len([i for i in range(len(self.__lines)) if self.__check_line(i)]))


Solution()
