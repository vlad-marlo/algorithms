from itertools import permutations


res = set()
all_s = 0
for i in permutations('НОБЕЛИЙ', r=7):
    word = ''.join(i)
    all_s+= 1
    if word[0] != 'Й' and 'ИЙО' not in word:
        res.add(word)

print(len(res), all_s)