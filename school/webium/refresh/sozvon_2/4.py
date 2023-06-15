def solution(data: list[list[int]]) -> int:
    count = 0
    for line in data:
        repeatable = [i for i in line if line.count(i) > 1]
        non_repeatable = [i for i in line if line.count(i) == 1]
        count += len(repeatable) != 0 and len(non_repeatable) != 0 and (
                (sum(repeatable) / len(repeatable)) > (sum(non_repeatable) / len(non_repeatable)))
    return count


print(solution([[int(x) for x in s.split(';')] for s in open('9_1.csv').readlines()]))
