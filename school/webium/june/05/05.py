from itertools import product, permutations


def is_palindrome(word: str) -> bool:
    return word == word[::-1]


def palindrome_is_accessible(word: str) -> bool:
    return any(i == i[::-1] for i in permutations(word))


words = [''.join(i) for i in product('КОМПЬЮТЕР', repeat=5) if palindrome_is_accessible(''.join(i))]
print(words)
print(len(set(words)))
