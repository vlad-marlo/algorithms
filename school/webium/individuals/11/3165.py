def read_data(filename: str) -> tuple[int, list[list[int]]]:
    with open(filename) as file:
        count, total = map(int, file.readline().strip().split())
        return total, [[int(x) for x in file.readline().strip().split()] for _ in range(count)]


def solution(kg_per_person: int, data: list[list[int]]) -> tuple[int, int]:
    data.sort(key=lambda x: x[0]/x[1], reverse=True)
    persons = [[0, kg_per_person] for _ in range(2)]
    for person_id in range(len(persons)):
        while persons[person_id][1]:
            for i in range(len(data)):
                if data[i][0] < persons[person_id][1]:
                    persons[person_id][1] -= data[i][0]
                    data[i][0] = 0
                    persons[person_id][0] += data[i][1]
                    data[i][1] = 0
                else:
                    persons[person_id][0] += persons[person_id][1] * (data[i][1] / data[i][0])
                    data[i][1] -= persons[person_id][1] * (data[i][1] / data[i][0])
                    data[i][0] -= persons[person_id][1]
                    persons[person_id][1] = 0
    return persons[0][0], persons[1][0]


print(solution(*read_data('26_3165.txt')))

