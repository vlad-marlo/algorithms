with open('26.txt') as file:
    data = [int(file.readline()) for _ in range(int(file.readline()))]
    data.sort(reverse=True)
    answer = [data[0]]
    for b in data[1:]:
        if answer[-1] - b >= 3:
            answer.append(b)
    print(len(answer), answer[-1])

