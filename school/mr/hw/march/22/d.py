with open('4.txt') as file:
    count, day_limit = map(int, file.readline().split())
    data = [int(file.readline()) for _ in range(count)]
    del count
    data.sort(reverse=True)
    days = data[:day_limit]
    assert len(days) == day_limit
    print(sum(days), min(days))
    # 95429 93
