def calculate_factorial_recursively(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * calculate_factorial_recursively(x - 1)


for i in range(0, 7):
    print(str(calculate_factorial_recursively(i)))

# Result:
#
# 1
# 1
# 2
# 6
# 24
# 120
# 720
#
# Process finished with exit code 0
