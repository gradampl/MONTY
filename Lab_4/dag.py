def add_squares(*params):
    sum = 0
    for i in range(0, len(params)):
        sum += params[i] ** 2
    return sum


print(str(add_squares(2, 3, 4)))
print(str(add_squares(-2, 0.33, -4, 1, 2)))

# Result:
#
# 29
# 25.1089
#
# Process finished with exit code 0
