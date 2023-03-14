with open('26_6759.txt') as f:
    data = [int(f.readline()) for _ in range(int(f.readline()))]
    data.sort()
    s = 0
    count = 0
    for i in range(0, 2 * len(data) // 3, 2):
        a, b, c = data[i], data[i + 1], data[len(data) - (1 + count)]
        s += b + c
        count += 1
    print(s)

    # for i in range(len(data) - 2):
    #     s += data[i + 1] + data[i + 2]
    # print(s)
