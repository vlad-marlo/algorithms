import math
import time


def check_num(num: int) -> bool:
    divs = set()
    for div in range(1, int(math.sqrt(num)) + 1):
        if num % div == 0:
            another_div = num // div
            if div % 2 == 1:
                divs.add(div)
            if another_div % 2 == 1:
                divs.add(another_div)
            if len(divs) > 5:
                return False
    return len(divs) == 5


start = time.time()

for _num in range(35_000_000, 40_000_000):
    if check_num(_num):
        print(_num)
end = time.time()
print(start - end)
