def calculate_average(**kwargs):
    sum = 0
    for k, v in kwargs.items():
        sum += v
    average = sum / len(kwargs)
    return average


citizens = {"Wieńczysław": 2.5, "Anastazy": 7.9, "Kleopatra": 12, "Krzesimir": 5.2, "Ernesta": 18}
patients = {"Maks": 23, "Fela": 90, "Hela": 45, "Mela": 11}

print(calculate_average(**citizens))
print(calculate_average(**patients))

# Result:
#
# 9.12
# 42.25
#
# Process finished with exit code 0
