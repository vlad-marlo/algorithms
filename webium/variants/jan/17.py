with open('17.txt') as f:
    data = list(map(int, f.readlines()))
    even = list(filter(lambda x: x % 2 == 0, data))
    avg_even = sum(even) / len(even)
    __count = 0
    __max = 0
    for i in range(len(data) - 1):
        a, b = data[i], data[i + 1]
        if (a % 3 == 0 or b % 3 == 0) and min(a, b) < avg_even:
            __count += 1
            __max = max(__max, a + b)
    print(__count, __max)