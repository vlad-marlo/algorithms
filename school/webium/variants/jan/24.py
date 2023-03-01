with open('24.txt') as f:
    data = f.read().strip()
    c = 0
    for i in range(len(data) - 4):
        string = data[i:i+5]
        c += string == string[::-1]
    print(c)

