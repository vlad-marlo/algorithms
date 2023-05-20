nums = [int(x) for x in open('17.txt')]
count = 0
min_sum = float('inf')
triples = [i for i in nums if 100 <= i < 1000]

for i in range(len(nums) - 1):
    a, b = nums[i:i + 2]
    if ((a in triples and b not in triples) or (b in triples and a not in triples)) and (a + b) % 115 == 0:
        count += 1
        min_sum = min(a + b, min_sum)
print(count, min_sum)
