f = open("27-B.txt")
s = f.readlines()
n = int(s[0])
sumAns = 0
sum2 = 0
sum3 = 0
minDif = 20001
for i in range(1, n + 1):
    x, y, z = map(int, s[i].split())
    if (x >= y) and (x >= z):
        sumAns = sumAns + x
        if y >= z:
            sum2 = sum2 + y
            sum3 = sum3 + z
        else:
            sum3 = sum3 + y
            sum2 = sum2 + z
        if ((abs(x - y)) % 2 != 0) and (abs(x - y) < minDif):
            minDif = abs(x - y)
        elif ((abs(x - z)) % 2 != 0) and (abs(x - z) < minDif):
            minDif = abs(x - z)
    elif (y >= z) and (y >= x):
        sumAns = sumAns + y
        if x >= z:
            sum2 = sum2 + x
            sum3 = sum3 + z
        else:
            sum3 = sum3 + x
            sum2 = sum2 + z
        if ((abs(y - x)) % 2 != 0) and (abs(y - x) < minDif):
            minDif = abs(y - x)
        elif ((abs(y - z)) % 2 != 0) and (abs(y - z) < minDif):
            minDif = abs(y - z)
    elif (z >= x) and (z >= y):
        sumAns = sumAns + z
        if x >= y:
            sum2 = sum2 + x
            sum3 = sum3 + y
        else:
            sum3 = sum3 + x
            sum2 = sum2 + y
        if ((abs(z - x)) % 2 != 0) and (abs(z - x) < minDif):
            minDif = abs(z - x)
        elif ((abs(z - y)) % 2 != 0) and (abs(z - y) < minDif):
            minDif = abs(z - y)
if (sum2 + sum3) % 2 != 0:
    print(sumAns)
else:
    print(sumAns - minDif)
