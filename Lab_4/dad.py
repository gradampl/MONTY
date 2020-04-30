def cg(n, a1, q):
    an = q ** (n - 1) * a1
    return an


print(str(cg(5, 1, 2)))
print(str(cg(4, 1, 3)))

# Example results:
#
# 16
# 27
#
# Process finished with exit code 0
