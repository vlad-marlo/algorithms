print(sum([sum([any(
        line[x] == line[n] or line[x + 4] == line[n + 4] for x in range(4) if x not in ((line.index(0) % 4), n))
        for n in range(4) if n != (line.index(0) % 4)]) for line in
        [list(map(int, x.strip().split(','))) for x in open('9.csv').readlines()] if
        line.count(0) == 1]))
