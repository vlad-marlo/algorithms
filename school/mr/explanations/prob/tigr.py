from functools import lru_cache


@lru_cache(None)
def game(p):
    return 0 if p >= 351 else 1 if any(p1 >= 351 for p1 in (p + 1, p + 4, p * 2)) \
        else 2 if all(game(p1) == 1 for p1 in (p + 1, p + 4, p * 2)) \
        else 3 if any(game(p1) == 2 for p1 in (p + 1, p + 4, p * 2)) \
        else 4 if all(game(p1) in (1, 3) for p1 in (p + 1, p + 4, p * 2)) else -1


for p in range(1, 350):
    print(f'19: {p}\n' if (res := game(p)) == 2 else f'20: {p}\n' if res == 3 else f'21: {p}\n' if res == 4 else "",
          end="")
