from math import sqrt


class Zespolone:
    def __init__(self, Rz, Im):
        self.Rz = Rz
        self.Im = Im

    def __add__(self, other):
        if isinstance(other, (float, int)):
            other = Zespolone(other)
        return Zespolone(self.Rz + other.Rz,
                         self.Im + other.Im)

    def __sub__(self, other):
        if isinstance(other, (float, int)):
            other = Zespolone(other)
        return Zespolone(self.Rz - other.Rz,
                         self.Im - other.Im)

    def __mul__(self, other):
        return Zespolone(self.Rz * other.Rz - self.Im * other.Im,
                         self.Im * other.Rz + self.Rz * other.Im)

    def __truediv__(self, other):
        r = float(other.Rz ** 2 + other.Im ** 2)
        return Zespolone((self.Rz * other.Rz + self.Im * other.Im) / r, (self.Im * other.Rz - self.Rz * other.Im) / r)

    def __abs__(self):
        return sqrt(self.Rz ** 2 + self.Im ** 2)

    def __neg__(self):  # defines -c (c is Complex)
        return Zespolone(-self.Rz, -self.Im)

    def __eq__(self, other):
        return self.Rz == other.Rz and self.Im == other.Im

    def __ne__(self, other):
        return not self.__eq__(other)

    def _illegal(self, op):
        print('Działanie "%s" nie jest wykonalne na liczbach zespolonych.' % op)

    def __gt__(self, other):
        self._illegal('>')

    def __ge__(self, other):
        self._illegal('>=')

    def __lt__(self, other):
        self._illegal('<')

    def __le__(self, other):
        self._illegal('<=')

    def __pow__(self, n):
        a = Zespolone(1, 0)
        for i in range(n):
            a = a.__mul__(self)
        return a

    def __str__(self):
        return '(%g, %g)' % (self.Rz, self.Im)

    def __repr__(self):
        return 'Z' + str(self)


x = Zespolone(2, 3)
y = Zespolone(4, 5)
print("x = " + repr(x))
print("y = " + repr(y))
z0 = Zespolone.__add__(x, y)
z1 = Zespolone.__sub__(x, y)
z2 = Zespolone.__sub__(y, x)
z3 = Zespolone.__mul__(x, y)
z4 = Zespolone.__mul__(y, x)
z5 = Zespolone.__truediv__(x, y)
z6 = Zespolone.__truediv__(y, x)
z7 = Zespolone.__abs__(x)
z8 = Zespolone.__abs__(y)
z9 = Zespolone.__pow__(x, 2)
z10 = Zespolone.__pow__(y, 2)
z11 = Zespolone.__neg__(x)
z12 = Zespolone.__neg__(y)
z13 = Zespolone.__le__(x, y)
z14 = Zespolone.__gt__(x, y)
z15 = Zespolone.__eq__(x, y)
z16 = Zespolone.__eq__(y, x)
z17 = Zespolone.__eq__(x, x)
z18 = Zespolone.__eq__(y, y)

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
print("Liczba sprzężona z x = " + repr(z11))
print("Liczba sprzężona z y = " + repr(z12))
print("x <= y " + repr(z13))
print("y <= x " + repr(z14))
print("x == y " + repr(z15))
print("y == x " + repr(z16))
print("x == x " + repr(z17))
print("y == y " + repr(z18))
