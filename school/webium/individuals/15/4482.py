def read_data(filename: str) -> list[int]:
    with open(filename) as file:
        return [int(file.readline()) for _ in range(int(file.readline()))]


def solution(data: list[int]) -> int:
    sm = int((sum(data)+1)//2)
    min_len = 10000000**100
    status = True
    for i in range(sm, sm * 2):
        if not status:
            break
        query_sum = 0
        left = 0
        leng = 1
        length = 100000000
        for right in range(len(data)):
            leng += 1
            query_sum += data[right]
            while query_sum > i:
                query_sum -= data[left % len(data)]
                left += 1
                leng -= 1
            if i == query_sum:
                length = min(length, leng, len(data)-leng)
                status = False
        if not status:
            min_len = length
    return min_len



print(solution(read_data('27A_4482.txt')))
print(solution(read_data('27B_4482.txt')))
