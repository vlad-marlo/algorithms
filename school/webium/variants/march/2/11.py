from math import log2, ceil

i = ceil((13 * ceil(log2(36))) / 8)
i += ceil((5 * ceil(log2(6)) + 2 * ceil(log2(10))) / 8)
print(30-i)
