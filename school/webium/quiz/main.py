# x = 2 * 34 ** 56 - 7 * 8 ** 9
# s = ''
# while x:
#     s += str(x % 8)
#     x //= 8
# s = s[::-1]
# print(s.count('7'))

x = 2 * 34 ** 56 - 7 * 8 ** 9
res = 0
while x:
    res += (x % 8) == 7
    x //= 8
print(res)