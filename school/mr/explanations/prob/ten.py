with open('10_6745.txt') as f:
    data = [i for i in f.read().strip().split() if i == 'вред']
    print(data)
    print(data.count('вред'))