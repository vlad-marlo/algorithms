f = open('26.txt')
count, n = map(int, f.readline().split())
data = [int(f.readline()) for _ in range(count)]
data.sort()
data = data[n:len(data)-n]
assert len(data) == count - n - n
print(max(data), sum(data)/len(data))
