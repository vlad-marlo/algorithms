import math
from typing import List


def get_dividers(num: int) -> List[int]:
    _res = []
    for div in range(1, int(math.sqrt(num))+1):
        if num % div == 0:
            _res.append(div)
            if div ** 2 != num:
                _res.append(num // div)
    return sorted(_res)


for i in range(164700, 164753):
    divs = get_dividers(i)
    if len(divs) == 6:
        print(*list(reversed(divs))[:2])
