print(sum([(len(set(i)) != len(i)) ^ (len([x for x in i if x % 2 != 0]) == 3) for s in open('51.csv').readlines() if (i := list(sorted(map(int, s.strip().split(',')))))]))
# 307
