def max_sum(data):
    res = [data[0]]
    for i in data[1:]:
        res.append(max(res[-1], i))
    return res


file = open('27_B_8513.txt')
k = int(file.readline())
n = int(file.readline())
data = [int(file.readline()) for _ in range(n)]
forward = max_sum(data)                 # макс до индекса i
backward = max_sum(data[::-1])[::-1]    # макс после индекса i
mx = 0
for i in range(n - k):
    mx = max(forward[i] + backward[i + k], mx)
print(mx)
