class Solution:
    def __init__(self):
        self.__data: list[int]
        self.__read_data('26.txt')
        self.__solution()
        print(self.__sum, self.__max_give, )
        self.__data: list[int]
        self.__read_data('26_test.txt')
        self.__solution()
        print(self.__sum, self.__max_give, )

    def __read_data(self, filename: str):
        with open(filename) as file:
            self.__data = [int(file.readline()) for _ in range(int(file.readline()))]

    def __solution(self):
        nums = self.__data
        self.__max_give = 0
        self.__sum = 0
        while nums:
            index = len(nums) - nums[::-1].index(max(nums)) - 1
            assert max(nums) == nums[index]
            self.__sum += (index + 1) * nums[index]
            self.__max_give = max(self.__max_give, (index + 1) * nums[index])
            if index + 1 == len(nums):
                break
            nums = nums[index + 1:]


Solution()
