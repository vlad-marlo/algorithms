data = [int(x) for x in open('17_5635.txt')]
end_31 = [i for i in data if str(i)[-2:] == '31']
abs_sum = abs(min(end_31) + max(end_31))

count = 0
max_summ = float('-inf')
for i in range(len(data) - 1):
    a, b = data[i:i+2]
    if a <= abs_sum or b <= abs_sum:
        continue
    count += 1
    max_summ = max(max_summ, a + b)

print(count, max_summ)
