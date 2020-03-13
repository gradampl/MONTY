i = 0
j = 0

while i < 6:
    j = 0
    while j < 6:
        print(i, '*', j, '=', i * j)
        j += 1
        if j % 6 == 0: print('\n')
    i += 1
    