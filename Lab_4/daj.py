def count_calls():
    count_calls.counter += 1
    print("I am called for the " + str(count_calls.counter) + " time.")


count_calls.counter = 0


def count_calls2(i=[0]):
    i[0] += 1
    print("And I am called for the " + str(i[0]) + " time.")


for i in range(10):
    count_calls()
    count_calls2()

# Result:

# I am called for the 1 time.
# And I am called for the 1 time.
# I am called for the 2 time.
# And I am called for the 2 time.
# I am called for the 3 time.
# And I am called for the 3 time.
# I am called for the 4 time.
# And I am called for the 4 time.
# I am called for the 5 time.
# And I am called for the 5 time.
# I am called for the 6 time.
# And I am called for the 6 time.
# I am called for the 7 time.
# And I am called for the 7 time.
# I am called for the 8 time.
# And I am called for the 8 time.
# I am called for the 9 time.
# And I am called for the 9 time.
# I am called for the 10 time.
# And I am called for the 10 time.
#
# Process finished with exit code 0
