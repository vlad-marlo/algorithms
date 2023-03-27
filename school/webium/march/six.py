print(*[i for i in range(128, 256) if i - int(bin(i)[2:].replace('1', '2').replace('0', '1').replace('2', '0'), 2) == 185])
