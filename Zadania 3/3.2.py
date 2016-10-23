#!/usr/bin/python
# -*- coding: iso-8859-2 -*-


print("a)")
#L = L.sort()
# Najpierw trzeba zainicjalizowac liste jakimis wartosciami
L = [1,3,2,5,4,7,6]
L.sort()
print(L)

print("b)")

# x, y = 1, 2, 3  za duzo wartosci w stosunku do zmiennych
# nalezy dodac zmienna, badz usunac jedna wartosc

x, y , z = 1, 2, 3
print(x,y,z)

print("c)")

#X = 1, 2, 3 ; X[1] = 4
# Tuple nie mozna zmieniac dlatego takie przypisanie jest niemozliwe
# Jedyna opcja to stworzenie nowego tuple z zadanymi wartosciami

X = (1, 2, 3)
print("Tuple:",X)
print("2 element tuple:",X[1])

print("d)")
#X = "abc" ; X.append("d")
# Funkcji append() mozemy uzyc do listy a nie do Stringa
X = "abc"
Y = X + "d"
print(Y)
#lub
T = ["a","b","c"]
T.append("d")
print(T)

print("d)")
map(pow, range(8))
print("kompiluje sie, funkcja map zwraca iterator")



