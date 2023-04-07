from string import punctuation


def convert_str(string: str) -> str:
    for i in punctuation:
        string = string.replace(i, '')
    return string.lower()

with open('10.txt') as file:
    data = list(map(convert_str, file.read().strip().split()))
    print(data.count('что')+data.count('как'))
