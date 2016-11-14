import math
import unittest
#from fractions import gcd  //fractions.gcd() is deprecated. Use math.gcd instead
#math.gcd = New in version 3.5.
#Wyniki zostaly wszedzie rzutowane na inty zeby bardziej przypominaly, ulamki
#w przypadku ujemnych ulamkow, minus dajemy do licznika, mianownik jest zawsze bez znaku

# frac1 + frac2
def add_frac(frac1,frac2):
    if(frac1[0] == 0) and (frac2[0] == 0):
        return [0, 0]
    if (frac1[1] == 0) and (frac2[1] == 0):
        return
    if(frac1[0] == 0 and frac2[0] != 0):
        return frac2
    if(frac1[0] != 0 and frac2[0] == 0):
        return frac1
    licznik = (frac1[0]*frac2[1])+(frac2[0]*frac1[1])
    mianownik = frac1[1] * frac2[1]
    if (math.gcd(licznik, mianownik) == 1):
        result = [int(licznik), int(mianownik)]
        return result

    else:
        NWD = math.gcd(licznik, mianownik)
        result = [int(licznik / NWD), int(mianownik / NWD)]
        return result

# frac1 - frac2
def sub_frac(frac1, frac2):
    if (frac1[0] == 0) and (frac2[0] == 0):
        return [0, 0]
    if (frac1[1] == 0) and (frac2[1] == 0):
        return
    if (frac1[0] == 0 and frac2[0] != 0):
        return frac2
    if (frac1[0] != 0 and frac2[0] == 0):
        return frac1
    licznik = (frac1[0] * frac2[1]) - (frac2[0] * frac1[1])
    mianownik = frac1[1] * frac2[1]


    if (math.gcd(licznik, mianownik) == 1):
        result = [int(licznik), int(mianownik)]
        return result

    else:
        NWD = math.gcd(licznik, mianownik)
        result = [int(licznik / NWD), int(mianownik / NWD)]
        return result

# frac1 * frac2
def mul_frac(frac1, frac2):
    if (frac1[0] == 0) and (frac2[0] == 0):
        return [0, 0]
    if (frac1[1] == 0) and (frac2[1] == 0):
        return
    if (frac1[0] == 0 and frac2[0] != 0):
        return frac2
    if (frac1[0] != 0 and frac2[0] == 0):
        return frac1
    licznik = frac1[0] * frac2[0]
    mianownik = frac1[1] * frac2[1]
    if (math.gcd(licznik, mianownik) == 1):
        result = [int(licznik), int(mianownik)]
        return result

    else:
        NWD = math.gcd(licznik, mianownik)
        result = [int(licznik / NWD), int(mianownik / NWD)]
        return result

# frac1 / frac2
def div_frac(frac1, frac2):
    if (frac1[0] == 0) and (frac2[0] == 0):
        return [0, 0]
    if (frac1[1] == 0) and (frac2[1] == 0):
        return
    if (frac1[0] == 0 and frac2[0] != 0):
        return frac2
    if (frac1[0] != 0 and frac2[0] == 0):
        return frac1
    licznik = frac1[0] * frac2[1]
    mianownik = frac1[1] * frac2[0]
    if (math.gcd(licznik, mianownik) == 1):
        result = [int(licznik), int(mianownik)]
        return result

    else:
        NWD = math.gcd(licznik, mianownik)
        result = [int(licznik / NWD), int(mianownik / NWD)]
        return result

def is_positive(frac):
    if(frac[0] != 0) and (frac[1] == 0):
        return
    elif(frac[0] == 0) and (frac[1] != 0):
        return
    elif(frac[0] > 0):
        return True
    else:
        return False

def is_zero(frac):
    if(frac[0] == 0) and (frac[1] == 0):
        return True
    elif(frac[0] == 0):
        return True
    elif(frac[1] == 0):
        return
    else:
        return False

def cmp_frac(frac1,frac2):
    if(frac1[1] == 0) or (frac2[1] == 0):
        return
    result1 = frac1[0] / frac1[1]
    result2 = frac2[0] / frac2[1]
    if(result1 > result2):
        return 1
    elif (result1 == result2):
        return 0
    elif (result1 < result2):
        return -1

def frac2float(frac):
    if(frac[1] == 0):
        return
    else:
        result = [float(frac[0]),float(frac[1])]
        return result

class TestFractions(unittest.TestCase):
    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([3, 8], [1, 3]), [17, 24])
        self.assertEqual(add_frac([48, 56], [54, 72]), [45, 28])
        self.assertEqual(add_frac([10, 24], [1, 3]), [3, 4])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(sub_frac([3, 8], [1, 3]), [1, 24])
        self.assertEqual(sub_frac([48, 56], [54, 72]), [3, 28])
        self.assertEqual(sub_frac([10, 24], [1, 3]), [1, 12])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(mul_frac([3, 8], [1, 3]), [1, 8])
        self.assertEqual(mul_frac([48, 56], [54, 72]), [9, 14])
        self.assertEqual(mul_frac([10, 24], [1, 3]), [5, 36])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])
        self.assertEqual(div_frac([3, 8], [1, 3]), [9, 8])
        self.assertEqual(div_frac([48, 56], [54, 72]), [8, 7])
        self.assertEqual(div_frac([10, 24], [1, 3]), [5, 4])

    def test_is_positive(self):
        self.assertEqual(is_positive([1, 2]), True)
        self.assertEqual(is_positive([-3, 8]),False)
        self.assertEqual(is_positive([48, 56]),True)
        self.assertEqual(is_positive([10, 0]),None)
        self.assertEqual(is_positive([0, 10]),None)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([0, 0], [0, 0]), None)
        self.assertEqual(cmp_frac([1, 0], [0, 0]), None)
        self.assertEqual(cmp_frac([0, 0], [1, 0]), None)
        self.assertEqual(cmp_frac([1, 0], [1, 0]), None)
        self.assertEqual(cmp_frac([0, 1], [0, 1]), 0)
        self.assertEqual(cmp_frac([1, 2], [0, 2]), 1)
        self.assertEqual(cmp_frac([5, 6], [7, 8]), -1)

    def test_frac2float(self):
        self.assertEqual(frac2float([0, 0]), None)
        self.assertEqual(frac2float([1, 0]), None)
        self.assertEqual(frac2float([0, 10]), [0.0, 10.0])
        self.assertEqual(frac2float([3, 5]), [3.0, 5.0])
        self.assertEqual(frac2float([-5, 1]), [-5.0, 1.0])
        self.assertEqual(frac2float([-1, 2]), [-1.0, 2.0])

def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
