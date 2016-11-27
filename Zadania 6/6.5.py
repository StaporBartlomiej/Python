import math
import unittest
#from fractions import gcd  //fractions.gcd() is deprecated. Use math.gcd instead
#math.gcd = New in version 3.5.
#Wyniki zostaly wszedzie rzutowane na inty zeby bardziej przypominaly, ulamki
#w przypadku ujemnych ulamkow, minus dajemy do licznika, mianownik jest zawsze bez znaku

class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        if(self.y == 0):
            raise ValueError("Bad arguments")
        if not (isinstance(self.x,int) or isinstance(self.y,int)):
            raise ValueError("Bad arguments")
        self.x = x
        self.y = y

    def __str__(self): # zwraca "x/y" lub "x" dla y=1
        if (self.y == 1):
            return str(self.x)
        else:
            return str(self.x/self.y)



    def __add__(self, other):
        if (self.x == 0) and (other.x == 0):
            return [0, 0]
        if (self.y == 0) and (other.y == 0):
            return
        if (self.x == 0 and other.x != 0):
            return other
        if (self.x != 0 and other.x == 0):
            return self
        licznik = (self.x * other.y) + (other.x * self.y)
        mianownik = self.y * other.y
        if (math.gcd(licznik, mianownik) == 1):
            #result = [int(licznik), int(mianownik)]
            return Frac(int(licznik),int(mianownik))
        else:
            NWD = math.gcd(licznik, mianownik)
            #result = [int(licznik / NWD), int(mianownik / NWD)]
            return Frac(int(licznik / NWD),int(mianownik / NWD))

    def __sub__(self, other):
        if (self.x == 0) and (other.x == 0):
            return [0, 0]
        if (self.y == 0) and (other.y == 0):
            return
        if (self.x == 0 and other.x != 0):
            return other
        if (self.x != 0 and other.x == 0):
            return self
        licznik = (self.x * other.y) - (other.x * self.y)
        mianownik = self.y * other.y
        if (math.gcd(licznik, mianownik) == 1):
            #result = [int(licznik), int(mianownik)]
            return Frac(int(licznik),int(mianownik))
        else:
            NWD = math.gcd(licznik, mianownik)
            #result = [int(licznik / NWD), int(mianownik / NWD)]
            return Frac(int(licznik / NWD),int(mianownik / NWD))

    def __mul__(self, other):
        if (self.x == 0) and (other.x == 0):
            return [0, 0]
        if (self.y == 0) and (other.y == 0):
            return
        if (self.x == 0 and other.x != 0):
            return other
        if (self.x != 0 and other.x == 0):
            return self
        licznik = self.x * other.x
        mianownik = self.y * other.y
        if (math.gcd(licznik, mianownik) == 1):
            #result = [int(licznik), int(mianownik)]
            return Frac(int(licznik),int(mianownik))
        else:
            NWD = math.gcd(licznik, mianownik)
            #result = [int(licznik / NWD), int(mianownik / NWD)]
            return Frac(int(licznik / NWD),int(mianownik / NWD))

    def __truediv__(self, other):
        if (self.x == 0) and (other.x == 0):
            return [0, 0]
        if (self.y == 0) and (other.y == 0):
            return
        if (self.x == 0 and other.x != 0):
            return other
        if (self.x != 0 and other.x == 0):
            return self
        licznik = self.x * other.y
        mianownik = self.y * other.x
        if (math.gcd(licznik, mianownik) == 1):
            #result = [int(licznik), int(mianownik)]
            return Frac(int(licznik),int(mianownik))
        else:
            NWD = math.gcd(licznik, mianownik)
            #result = [int(licznik / NWD), int(mianownik / NWD)]
            return Frac(int(licznik / NWD),int(mianownik / NWD))



    def __cmp__(self, other):
        if (self.y == 0) or (other.y == 0):
            return
        result1 = self.x / self.y
        result2 = other.x / other.y
        if (result1 > result2):
            return 1
        elif (result1 == result2):
            return 0
        elif (result1 < result2):
            return -1

    def __float__(self):
        if (self.y == 0):
            return
        else:
            #result = [float(self.x), float(self.y)]
            return Frac(float(self.x),float(self.y))

            # operatory jednoargumentowe

    def __pos__(self):  # +frac = (+1)*frac
            return self

    def __neg__(self):  # -frac = (-1)*frac
            return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
            return Frac(self.y, self.x)

    def __repr__(self):
        return Frac(self.x,self.y)




a = Frac(2,1)
b = Frac(1,2)
c = Frac(5,3)
class TestFractions(unittest.TestCase):


    def test__self__(self):
        self.assertEqual(str(a), '2')
        self.assertEqual(str(b), '0.5')

    def test__add__(self):
        self.assertEqual(a+b, [5,2])
        self.assertEqual(a+c, [11,3])

    def test__sub__(self):
        self.assertEqual(c-b, [7,6])
        self.assertEqual(a-b, [3,2])

    def test__mul__(self):
        self.assertEqual(c*b, [5,6])
        self.assertEqual(c*a, [10,3])

    def test__div__(self):
        self.assertEqual(c/b, [10,3])
        self.assertEqual(b/c, [3,10])

    def test__repr__(self):
        self.assertEqual(repr(c),'(5, 3)')
        self.assertEqual(repr(b),'(1, 2)')
        self.assertEqual(repr(a),'(2, 1)')

    def test__pos__(self):
        self.assertEqual(repr(c),'(5, 3)')
        self.assertEqual(repr(b),'(1, 2)')
        self.assertEqual(repr(a),'(2, 1)')

    def test__neg__(self):
        self.assertEqual(str(-c),'(-5, 3)')
        self.assertEqual(str(-b),'(-1, 2)')
        self.assertEqual(str(-a),'(-2, 1)')

    def test__invert__(self):
        self.assertEqual(c.__invert__(),'(3, 5)')
        self.assertEqual(b.__invert__(),'(2, 1)')
        self.assertEqual(a.__invert__(),'(1, 2)')

#https://docs.python.org/3.0/whatsnew/3.0.html
#The cmp() function should be treated as gone, and the __cmp__() special method is no longer supported.
# Use __lt__() for sorting, __eq__() with __hash__(), and other rich comparisons as needed.
# (If you really need the cmp() functionality, you could use the expression (a > b) - (a < b) as the equivalent for cmp(a, b).)
#  def test__cmp__(self):


    def test__float__(self):
        self.assertEqual(float(0), 0.0)
        self.assertEqual(float(1), 1.0)
        self.assertEqual(float(3), 3.0)


def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
