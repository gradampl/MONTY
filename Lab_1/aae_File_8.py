import math

################################## Function #######################################

def give_coeficient(x):

    if x == 'a':
       abc = 'a'
    elif x == 'b':
        abc = 'b'
    else:
        abc = 'c'

    ok = False

    while ok == False:
        coef = input('Podaj współczynnik '+ str(abc)+':\n')
        try:
            ok = float(coef)
            return float(coef)
        except ValueError:
            print('Nie znam takiej liczby.\n')

    return float(coef)

###########################################################################


print('Rozwiążę równanie kwadratowe postaci ax^2 + bx + c = 0.')
print()

a = give_coeficient('a')

while a == 0:
    print("Jeśli a = 0, to równanie nie jest kwadratowe.")
    a = give_coeficient('a')

b = give_coeficient('b')
c = give_coeficient('c')

delta = b**2 - 4*a*c

if delta < 0: print('Równanie nie ma rozwiązań w zbiorze liczb rzeczywistych.')
elif delta == 0: print('Równanie ma jedno rozwiązanie: x1 = x2 =', -1*b / 2*a)
else:
    x1 = (-1*b - math.sqrt(b**2 - 4*a*c)) / 2*a
    x2 = (-1*b + math.sqrt(b**2 - 4*a*c)) / 2*a
    print('Równanie ma dwa rozwiązania: x1 =', x1, ', x2 =', x2)
