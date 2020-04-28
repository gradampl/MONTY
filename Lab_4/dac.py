def calculate_factorial_recursively(x):
    a = x
    if a == 0 or a == 1:
        return 1
    else:
        return a * calculate_factorial_recursively(a - 1)


for i in range (1,7):
    print(str(calculate_factorial_recursively(i)))


# Result:
#
# 1
# 2
# 6
# 24
# 120
# 720
#
# Process finished with exit code 0