def add(x, y):
    sum = x + y
    return sum


def get_number(param):
    ok = False
    a = int(param)
    text = None
    if a == 1:
        text = "pierwszą"
    else:
        text = "drugą"

    while ok == False:
        num = input('Podaj ' + text + ' liczbę całkowitą: \n')
        try:
            ok = int(num)
            if int(num) == 0:
                ok = True
        except ValueError:
            print('Nie znam takiej liczby całkowitej.\n')
    return int(num)


def greeting():
    print("\nJeśli podasz mi 2 liczby całkowite, powiem Ci, ile wynosi ich suma.\n")


def start():
    greeting()
    x = get_number(1)
    y = get_number(2)
    print("Suma liczb " + str(x) + " i " + str(y) + " wynosi " + str(add(x, y)))


##############################################################################

start()

# Result example:
#
# Jeśli podasz mi 2 liczby całkowite, powiem Ci, ile wynosi ich suma.
#
# Podaj pierwszą liczbę całkowitą:
# liczba całkowita
# Nie znam takiej liczby całkowitej.
#
# Podaj pierwszą liczbę całkowitą:
# 0.999999999999999999999999
# Nie znam takiej liczby całkowitej.
#
# Podaj pierwszą liczbę całkowitą:
# -1,9999999
# Nie znam takiej liczby całkowitej.
#
# Podaj pierwszą liczbę całkowitą:
# d
# Nie znam takiej liczby całkowitej.
#
# Podaj pierwszą liczbę całkowitą:
# -123
# Podaj drugą liczbę całkowitą:
# 912
# Suma liczb -123 i 912 wynosi 789
#
# Process finished with exit code 0

#########################################################

# Jeśli podasz mi 2 liczby całkowite, powiem Ci, ile wynosi ich suma.
#
# Podaj pierwszą liczbę całkowitą:
# 1/2
# Nie znam takiej liczby całkowitej.
#
# Podaj pierwszą liczbę całkowitą:
# 0
# Podaj drugą liczbę całkowitą:
# 0
# Suma liczb 0 i 0 wynosi 0
#
# Process finished with exit code 0
