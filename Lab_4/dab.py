def calculate_factorial(x):
    # a = x
    if x==0 or x==1:
        return 1
    else:
        factorial = 1
        i = 1
        while i <= x:
            factorial *= i
            i += 1
    return factorial

for i in range(0,7):
    print(str(calculate_factorial(i)))

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