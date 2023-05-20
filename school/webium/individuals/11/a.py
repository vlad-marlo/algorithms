def read_data(filename: str) -> tuple[int, list[list[int]]]:
    with open(filename) as file:
        count, total = map(int, file.readline().strip().split())
        return total, [[int(i) for i in file.readline().strip().split()] for _ in range(count)]


def solution(total: int, data: list[list[int]]) -> tuple[int, int]:
    dif = [x[0] for x in data]
    min_super = sum(dif) / len(dif)
    non_super = sorted([x[1] for x in data if x[0] <= min_super], reverse=True)
    supers = sorted([x[1] for x in data if x[0] > min_super], reverse=True)
    sm = 0
    time_for_supers = 0
    count_of_supers = 0
    last = 0
    last_super = False
    while (new_sm := sm + (supers.pop() if not last_super else non_super.pop())) <= total:
        last = new_sm - sm
        sm = new_sm
        last_super = not last_super
        if last_super:
            time_for_supers += last
        count_of_supers += 1
    if last_super:
        time_for_supers -= last
        count_of_supers -= 1
        sm -= last
        while (new_sm := sm + non_super.pop()) <= total:
            count_of_supers += 1
            sm = new_sm
    return count_of_supers, time_for_supers


print(solution(*read_data('26_4408.txt')))