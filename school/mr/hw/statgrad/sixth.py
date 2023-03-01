import string

with open('6.txt', ) as f:
    data = f.read().strip()
    SUB = 'DANOV'
    seqs = [SUB[0:i] + letter + SUB[i + 1:] for i in range(len(SUB)) for letter in string.ascii_uppercase if
            SUB[i] != letter]
    counter, _max = 0, 0
    for x in range(5):
        for i in range(x, len(data) - 5 - x, 5):
            sub = data[i:i + 5]
            if sub not in seqs:
                _max = max(counter + 4, _max)
                counter = 0
            else:
                counter += 1
    print(_max)
