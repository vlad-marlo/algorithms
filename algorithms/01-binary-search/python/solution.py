class Solution:
    def binary_search(self, seq, item) -> int:
        low = 0
        high = len(seq) - 1
        while low <= high:
            mid = (low + high) // 2
            guess = seq[mid]
            if guess == item:
                return mid
            if guess > item:
                high = mid - 1
            else:
                low = mid + 1
        return -1

if __name__ == '__main__':
    bs = Solution()
    my_list = [1, 3, 5, 7, 9]
    for index, item in enumerate(my_list):
        assert (res := bs.binary_search(my_list, item)) == index, f'got: {res}; want: {index}'
