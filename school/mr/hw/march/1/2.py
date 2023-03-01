import math


def read_data() -> list[int]:
    with open('2.txt') as file:
        return list(map(int, file.readlines()))


def solution(data: list[int]) -> int:
    __count = 0
    print(len(data))
    for i in range(len(data) - 2):
        lcm = math.lcm(*data[i:i + 3])
        for div in range(2, int(lcm ** 0.5) + 1):
            if lcm % div == 0:
                break
        else:
            __count += 1
    return __count


print(solution(read_data()))
# output - 9
