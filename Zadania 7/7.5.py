from points import Point
from math import pi
from math import pow
from math import sqrt



class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x=0, y=0, radius=1):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):      # "Circle(x, y, radius)"
        return "Circle(" + str(self.pt.getX()) + ", " + str(self.pt.getY())  + ", " + str(self.radius) + ")"
    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):            # pole powierzchni
        result = round(pi * pow(self.radius,2))
        return result

    def move(self, x, y):      # przesuniecie o (x, y)
        if not (isinstance(x,int) or isinstance(x,float)):
            raise ValueError("Bar argument")
        if not (isinstance(y,int) or isinstance(y,float)):
            raise ValueError("Bad arguments")
        newX = self.pt.getX() + x
        newY = self.pt.getY() + y
        self.pt.setX(newX)
        self.pt.setY(newY)
        return self


    def cover(self, other):    # okrąg pokrywający oba
        centerX = (self.pt.getX() + other.pt.getX()) / 2
        centerY = (self.pt.getY() + other.pt.getY()) / 2
        center = Point(centerX,centerY)
        if self.radius > other.radius:
            bigCircle = self
        else:
            bigCircle = other
        equation = round(sqrt(pow(bigCircle.pt.getX() - center.getX(), 2) + pow(bigCircle.pt.getY() - center.getY(), 2)),2)
        result = Circle(center.getX(), center.getY(), equation + bigCircle.radius)
        return result
# Kod testujący moduł.
a = Circle(1, -4, 3)
b = Circle(2 , 2, 4)
c = Circle(1, -4, 3)
d = Circle(3, -3, 2)
e = Circle(5, 2, 0)
f = Circle(1, 0, 1)
g = Circle(3, 1, 2)
h = Circle(0, 0, 2)

import unittest

class TestCircle(unittest.TestCase):

    def test__repr__(self):
        self.assertEqual(repr(a), "Circle(1, -4, 3)")
        self.assertEqual(repr(b), "Circle(2, 2, 4)")
        self.assertEqual(repr(c), "Circle(1, -4, 3)")

    def test__eq__(self):
        self.assertEqual(a == b, False)
        self.assertEqual(a == c, True)
        self.assertEqual(a == d, False)

    def test__neq__(self):
        self.assertEqual(a != b, True)
        self.assertEqual(a != c, False)
        self.assertEqual(a != c, False)

    def test__area(self):
        self.assertEqual(a.area(), 28)
        self.assertEqual(b.area(), 50)

    def test__move(self):
        self.assertEqual(e.move(-2, 3), Circle(3, 5, 0))
        self.assertEqual(d.move(-1, 2), Circle(2, -1, 2))

    def test__cover(self):
        self.assertEqual(f.cover(g), Circle(2.0, 0.5, 3.12))
        self.assertEqual(f.cover(h), Circle(0.5, 0, 2.5))

if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy