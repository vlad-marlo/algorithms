def get_count_from_i(data: list[int], index: int, less: int) -> int:
    _sum = [data[index]]
    while sum(_sum) <= less and index + 1< len(data):
        index += 1
        _sum.append(data[index])
    if len(_sum) == 1340:
        print(max(_sum))
    return len(_sum) - 1


f = open('5050d83d-e4f5-4236-838e-a5a93dcfd0de.txt')
less = int(f.readline().split()[0])
data = list(map(int, f.readlines()))
_max = 0
for i in range(len(data)):
    _max = max(_max, get_count_from_i(data, i, less))
print(_max)
