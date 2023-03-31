def binary_search(__seq: list[int | float], __item: int | float) -> int:
    low = 0
    high = len(__seq) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = __seq[mid]
        if guess == __item:
            return mid
        if guess > __item:
            high = mid - 1
        else:
            low = mid + 1
    return -1


if __name__ == '__main__':
    my_list = [1, 3, 5, 7, 9]
    for index, item in enumerate(my_list):
        assert (res := binary_search(my_list, item)) == index, f'got: {res}; want: {index}'
