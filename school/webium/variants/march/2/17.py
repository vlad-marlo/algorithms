nums = [i for i in range(2020,647038+1) if sum(int(x) for x in str(i)) < 10 and str(min(int(x) for x in str(i))) not in str(i)[:3]]
avg = sum(nums) / len(nums)
most_common = min([i for i in range(len(nums))], key=lambda x: abs(nums[x] - avg))
print( len(nums), nums[most_common],)