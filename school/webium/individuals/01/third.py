with open('26_4115.txt') as f:
    n = int(f.readline())
    data = list(set([tuple(map(int, f.readline().split())) for _ in range(n)]))
    data.sort()
    dict_data: dict[int, list] = {}
    for key, value in data:
        if dict_data.get(key) is None:
            dict_data[key] = []
        dict_data[key].append(value)
    _max = 0
    _key = 10000000
    for key, value in dict_data.items():
        value.sort()
        local_counter = 1
        for i in range(len(value) - 1):
            if value[i] + 1 == value[i + 1]:
                local_counter += 1
                if local_counter > _max:
                    _max = local_counter
                    _key = key
            else:
                local_counter = 1
    print(dict_data[_key-2])
    print(_max, _key)



