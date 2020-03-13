import math

print('Rozwiążę równanie kwadratowe postaci ax^2 + bx + c = 0.')
print()
a = float(input('Podaj współczynnik a (tzn. współczynnik przy x^2). \n'))

while a == 0:
    print("Jeśli a = 0, to równanie nie jest kwadratowe.")
    a = int(input('Podaj współczynnik a \n'))

b = float(input('Podaj współczynnik b (tzn. współczynnik przy x).\n'))
c = float(input('Podaj współczynnik c (tzn. wyraz wolny równania)\n'))

delta = b**2 - 4*a*c

if delta < 0: print('Równanie nie ma rozwiązań w zbiorze liczb rzeczywistych.')
elif delta == 0: print('Równanie ma jedno rozwiązanie: x1 = x2 =', -1*b / 2*a)
else:
    x1 = (-1*b - math.sqrt(b**2 - 4*a*c)) / 2*a
    x2 = (-1*b + math.sqrt(b**2 - 4*a*c)) / 2*a
    print('Równanie ma dwa rozwiązania: x1 =', x1, ', x2 =', x2)
