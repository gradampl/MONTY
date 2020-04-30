def cube(*args):
    cubes = [args[x] ** 3 for x in range(0, len(args))]
    return cubes

print(cube(2, 3, 4))
print(cube(-2, 0.33, -4, 1, 2))