from math import sqrt
import unittest

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):  # zwraca string "(x, y)"
        return '(' + str(self.x) + ',' + str(self.y) + ')'

    def __repr__(self):  # zwraca string "Point(x, y)"
        return "Point" + str(self)

    def __eq__(self, other):  # obsługa point1 == point2
        if (self.x == other.x) and (self.y == other.y):
            return True
        else:
            return False

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    def __add__(self, other):  # v1 + v2
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):  # v1 - v2
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny
        return (self.x * other.x) + (self.y * other.y)

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D
        return self.x * other.y - self.y * other.x

    def length(self):  # długość wektora
        result = sqrt((self.x * self.x) + (self.y * self.y))
        return round(result,2)

a = Point(4,6)
b = Point()
c = Point(7.63,-2)
d = Point(4,6)






class TestPoint(unittest.TestCase):

    def test__str__(self):
        self.assertEqual(str(a), '(4,6)')
        self.assertEqual(str(b), '(0,0)')
        self.assertEqual(str(c), '(7.63,-2)')

    def test__repr__(self):
         self.assertEqual(repr(a), 'Point(4,6)')
         self.assertEqual(repr(b), 'Point(0,0)')
         self.assertEqual(repr(c), 'Point(7.63,-2)')

    def test__eq__(self):
         self.assertEqual(a == b, False)
         self.assertEqual(a == c, False)
         self.assertEqual(a == d, True)

    def test__ne__(self):
         self.assertEqual(a != b, True)
         self.assertEqual(a != c, True)
         self.assertEqual(a != d, False)

    def test__add__(self):
         self.assertEqual(str(Point(4,6) + Point()), '(4,6)')
         self.assertEqual(str(Point(4,6) + Point(4,6)), '(8,12)')
         self.assertEqual(str(Point(4,6) + Point(2.56, -4)), '(6.5600000000000005,2)')

    def test__sub__(self):
         self.assertEqual(str(Point(4,6) - Point()), '(4,6)')
         self.assertEqual(str(Point() - Point(4,6)), '(-4,-6)')
         self.assertEqual(str(Point(4,6) - Point(2,4)), '(2,2)')

    def test__mul__(self):
        self.assertEqual(Point(4,6) * Point(), 0)
        self.assertEqual(Point() * Point(4,6), 0)
        self.assertEqual(Point(4,6) * Point(2,2), 20)

    def test__cross(self):
        self.assertEqual(Point.cross(Point(4,6), Point()), 0)
        self.assertEqual(Point.cross(Point(4,6), Point(4,6)), 0)
        self.assertEqual(Point.cross(Point(4,6), Point(3, 1)), -14)

    def test__length(self):
        self.assertEqual(Point.length(Point(4,6)), 7.21)
        self.assertEqual(Point.length(Point(0, 5)), 5)
        self.assertEqual(Point.length(Point(6, 0)), 6)

if __name__ == '__main__':
        unittest.main()  # uruchamia wszystkie testy
