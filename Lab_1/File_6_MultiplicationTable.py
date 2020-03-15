
i = 0
while i < 6:
    j = 0
    while j < 6:
        if j == 0:
            print('\n', end='')
        else:
            print('     ',end='')
        print(i, '*', j, '=', "%2d"%(i*j), end='')
        j += 1
    i += 1





# dwa wiersze po trzy słupki

# k = 0
# while k < 2:
#     print()
#     i = 0
#     while i < 6:
#         j = 0
#         while j < 3:
#             if j == 0:
#                 print('\n', end='')
#             else:
#                 print('     ',end='')
#             print(j+3*k, '*', i, '=', "%2d"%((j+3*k) * i), end='')
#             j += 1
#         i += 1
#     k += 1
