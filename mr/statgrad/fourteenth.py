# import string
#
# alp = string.digits + string.ascii_uppercase
# print(alp)
# for p in range(10, 37):
#     for x in alp[:p]:
#         for y in alp[:p]:
#             if int(f'32{x}8', p) + int(f'{x}{x}{x}9', p) == int(f'{y}{y}02', p):
#                 print(int(f'{y}{y}{x}', p))

print(*[int(f'{y}{y}{x}', p) for p in range(10, 36) for y in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:p] for x in
        '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:p] if int(f'32{x}8', p) + int(f'{x}{x}{x}9', p) == int(f'{y}{y}02', p)])
