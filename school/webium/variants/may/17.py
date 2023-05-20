nums = [int(x) for x in open('17.txt')]
max_54 = max([x for x in nums if abs(x) % 100 == 54])
c = 0
mx = 0
for i in range(len(nums) - 1):
    a, b = nums[i:i + 2]
    if abs(a) % 100 == abs(b) % 100 and abs(a) + abs(b) <= max_54:
        c += 1
        mx = max(mx, a, b)
print(c, mx)
