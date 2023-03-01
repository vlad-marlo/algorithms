num = 4 * 8 ** 3032 + 3 * 16 ** 1956 + 870

triples = 0
ones = 0
while num:
    n = num % 7
    triples += n == 3
    ones += n == 1
    num //= 7
print(triples * 3 - ones)
