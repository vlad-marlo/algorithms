from collections import Counter

s = open('24vlad2.txt').readlines()
ans_letter = ''
ans_count = 0
for line_i, line in enumerate(s):
    letter = line[0]
    counter = 1
    ans = 0
    last = line[0]
    for i in line[1:]:
        if i != last:
            counter = 0
        else:
            counter += 1
            if ans > counter:
                ans = counter
                letter = i
            elif ans == counter:
                letter = min(letter, i)
        last = i
    if ans > ans_count:
        ans_letter = letter
print(ans_letter, open('24vlad2.txt').read().count(ans_letter), sep='')
