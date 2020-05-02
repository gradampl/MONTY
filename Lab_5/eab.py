from math import sqrt


class Zespolone:

    def __init__(self, Rz, Im):
        self.Rz = Rz
        self.Im = Im

    def __add__(self, other):
        return Zespolone(self.Rz + other.Rz,
                         self.Im + other.Im)

    def __sub__(self, other):
        return Zespolone(self.Rz - other.Rz,
                         self.Im - other.Im)

    def __mul__(self, other):
        return Zespolone(self.Rz * other.Rz - self.Im * other.Im,
                         self.Im * other.Rz + self.Rz * other.Im)

    def __div__(self, other):
        r = float(other.Rz ** 2 + other.Im ** 2)
        return Zespolone((self.Rz * other.Rz + self.Im * other.Im) / r, (self.Im * other.Rz - self.Rz * other.Im) / r)

    def __abs__(self):
        return sqrt(self.Rz ** 2 + self.Im ** 2)

    def __conj__(self):
        return Zespolone(self.Rz, -self.Im)

    def __eq__(self, other):
        return self.Rz == other.Rz and self.Im == other.Im

    def __ne__(self, other):
        return not self.__eq__(other)

    def _illegal(self, operation):
        return 'Działanie "%s" nie jest wykonalne na liczbach zespolonych.' % operation

    def __gt__(self, other):
        return self._illegal(">")

    def __ge__(self, other):
        return self._illegal(">=")

    def __lt__(self, other):
        return self._illegal("<")

    def __le__(self, other):
        return self._illegal("<=")

    def __pow__(self, n):
        a = Zespolone(1, 0)
        for i in range(n):
            a = a.__mul__(self)
        return a

    def __str__(self):
        return '(%g, %g)' % (self.Rz, self.Im)

    def __repr__(self):
        return str(self)


x = Zespolone(2, 3)
y = Zespolone(4, 5)
print("x = " + repr(x))
print("y = " + repr(y))
z0 = Zespolone.__add__(x, y)
z1 = Zespolone.__sub__(x, y)
z2 = Zespolone.__sub__(y, x)
z3 = Zespolone.__mul__(x, y)
z4 = Zespolone.__mul__(y, x)
z5 = Zespolone.__div__(x, y)
z6 = Zespolone.__div__(y, x)
z7 = Zespolone.__abs__(x)
z8 = Zespolone.__abs__(y)
z9 = Zespolone.__pow__(x, 2)
z10 = Zespolone.__pow__(y, 2)
z11 = Zespolone.__conj__(x)
z12 = Zespolone.__conj__(y)
z13 = Zespolone.__le__(x, y)
z14 = Zespolone.__gt__(x, y)
z15 = Zespolone.__eq__(x, y)
z16 = Zespolone.__eq__(y, x)
z17 = Zespolone.__eq__(x, x)
z18 = Zespolone.__eq__(y, y)
z19 = Zespolone.__ne__(x, y)

print("x + y = " + repr(z0))
print("x - y = " + repr(z1))
print("y - x = " + repr(z2))
print("x * y = " + repr(z3))
print("y * x = " + repr(z4))
print("x / y = " + repr(z5))
print("y / x = " + repr(z6))
print("Moduł x = " + repr(z7))
print("Moduł y = " + repr(z8))
print("x do potęgi 2 = " + repr(z9))
print("y do potęgi 2 = " + repr(z10))
print("Liczba sprzężona do x = " + repr(z11))
print("Liczba sprzężona do y = " + repr(z12))
print("x <= y " + repr(z13))
print("y > x " + repr(z14))
print("x == y " + repr(z15))
print("y == x " + repr(z16))
print("x == x " + repr(z17))
print("y == y " + repr(z18))
print("x != y " + repr(z19))


# Result:
#
# x = (2, 3)
# y = (4, 5)
# x + y = (6, 8)
# x - y = (-2, -2)
# y - x = (2, 2)
# x * y = (-7, 22)
# y * x = (-7, 22)
# x / y = (0.560976, 0.0487805)
# y / x = (1.76923, -0.153846)
# Moduł x = 3.605551275463989
# Moduł y = 6.4031242374328485
# x do potęgi 2 = (-5, 12)
# y do potęgi 2 = (-9, 40)
# Liczba sprzężona z x = (2, -3)
# Liczba sprzężona z y = (4, -5)
# x <= y 'Działanie "<=" nie jest wykonalne na liczbach zespolonych.'
# y > x 'Działanie ">" nie jest wykonalne na liczbach zespolonych.'
# x == y False
# y == x False
# x == x True
# y == y True
# x != y True
#
# Process finished with exit code 0
