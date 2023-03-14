with open('26_1.txt') as f:
    c, count_of_users = map(int, f.readline().split())
    data = [int(f.readline()) for _ in range(count_of_users)]
    data.sort()
    _u = 0
    seq = []
    for val in data:
        if (sum(seq) + val) > c:
            break
        seq.append(val)
        _u += 1
    seq.pop(len(seq) - 1)
    _max = 0
    for i in reversed(range(c - sum(seq) + 1)):
        if i in data:
            _max = i
            break
    print(_u, _max)


