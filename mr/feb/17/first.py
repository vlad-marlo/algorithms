# https://inf-ege.sdamgia.ru/problem?id=46983
import math
import time


def get_fifth_divider(num: int) -> int:
    c = 0
    for i in range(2, int(math.sqrt(num)) + 1):
        c += num % i == 0
        if c == 5:
            print(num // i)
            return 1
    return 0


start = time.time()
count = 0
num = 460000001
while count < 5:
    count += get_fifth_divider(num)
    num += 1
end = time.time()
print(end - start)
