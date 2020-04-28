def calculate_factorial(x):
    a = x
    factorial = 1
    i = 1
    while i <= a:
        factorial *= i
        i += 1
    return factorial

for i in range(1,7):
    print(str(calculate_factorial(i)))

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