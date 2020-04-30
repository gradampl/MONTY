def sort_check(list):
    for i in range(0, len(list)):
        print(list)
        if list[i] <= list[i + 1]:
            return False
        else:
            return True


list1 = [1, 2, 3, 4, 5]
list2 = [5, 5, 5, 5, 5]
list3 = [5, 5, 4, 4, 3]
list4 = [5, 4, 3, 2, 1]

print(sort_check(list1))
print(sort_check(list2))
print(sort_check(list3))
print(sort_check(list4))

# Result:
#
# [1, 2, 3, 4, 5]
# False
# [5, 5, 5, 5, 5]
# False
# [5, 5, 4, 4, 3]
# False
# [5, 4, 3, 2, 1]
# True
#
# Process finished with exit code 0
