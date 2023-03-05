def ans(n, g, e):
    if n == g:
        return 1
    if n > g or n == e:
        return 0
    return ans(n + 1, g, e) + ans(n * 2, g, e)


print(ans(2, 11, 26)*ans(11, 39, 26))
