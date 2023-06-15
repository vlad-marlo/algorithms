def read_data(filename: str) -> list[int]:
    with open(filename) as file:
        return [int(file.readline()) for _ in range(int(file.readline()))]


def calculate_ans_if_ok(sm: int, index: int, ans: int, ans_sm: int) -> tuple[int, int]:
    if ans_sm < sm:
        return index + 1, sm
    if ans_sm > sm:
        return ans, ans_sm
    return min(index + 1, ans), ans_sm


def solution(data: list[int]) -> int:
    sm = 0
    m = 69
    ans = 0
    ans_sm = 0
    prefixes = [(10 ** 10, 0) for _ in range(m)]
    for index, item in enumerate(data):
        sm += item
        if (key := sm % m) == 0:
            ans, ans_sm = calculate_ans_if_ok(sm, index, ans, ans_sm)
            continue
        prefix_sm, prefix_index = prefixes[key]
        got_sm = sm - prefix_sm
        got_length = index - prefix_index + 1
        if ans_sm <= got_sm:
            if ans_sm == got_sm:
                ans = min(got_length, ans)
                continue
            ans = got_length
            ans_sm = got_sm
        prefixes[key] = max((sm, index), prefixes[key], key=lambda x: (x[0], x[1]))
    return ans


class Solution:
    DIVISOR = 69

    def __init__(self, filename: str) -> None:
        self.__ans = 0
        self.__prefixes = []
        self.__ans_sum: int = 0
        self.__sm: int = 0
        self.__data = self.__read_data(filename)
        return

    def solution(self) -> int:
        self.__prefixes = [(10 ** 10, 0) for _ in range(self.DIVISOR)]
        self.__ans = 0
        self.__ans_sum = 0
        self.__sm = 0
        for index, item in enumerate(self.__data):
            self.__do_iteration(index, item)
        return self.__ans

    @staticmethod
    def __read_data(_filename: str) -> list[int]:
        with open(_filename) as file:
            return [int(file.readline()) for _ in range(int(file.readline()))]

    def __do_iteration(self, index, item):
        self.__sm += item
        if (key := self.__sm % self.DIVISOR) == 0:
            if self.__ans_sum < self.__sm:
                self.__ans = index + 1
                self.__ans_sum = self.__sm
                return
            if self.__ans_sum == self.__sm:
                self.__ans = min(index + 1, self.__ans)
            return


print(solution(read_data('27A.txt')))
print(solution(read_data('27B.txt')))
print(solution(read_data('test')))
