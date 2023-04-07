with open('9_6925.csv') as file:
    data = [list(map(int, x.strip().split(';'))) for x in file.readlines()]
    c = 0
    for line in data:
        if len(set(line))+1 != len(line):
            continue
        odd = []
        even = []
        for i in line:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        avg_odd = 0 if len(odd) == 0 else sum(odd)/len(odd)
        avg_even = 0 if len(even) == 0 else sum(even)/len(even)
        if avg_even - 50 > avg_odd:
            c += 1
    print(c)

