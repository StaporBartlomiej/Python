#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

print("a)")
x = 2 ; y = 3;  #zbedny srednik na koncu
if (x > y):  # niepotrzebne nawiasy
    result = x;  #zbedny srednik na koncu
    print(result)
else:
    result = y;  #zbedny srednik na koncu
    print(result)

#Tak, jest poprawny chociaz sredniki sa w 3 miejsach zbedne
#Oraz jesli chcemy zainicjalizowac zmienne to zrobilbym to
#w odstepnych liniach:
# x = 2
# y = 3


print("b)")
#for i in "qwerty": if ord(i) < 100: print i # tu jest zle, powinno byc tak:

for i in "qwerty":  # poniewaz kazda litera w tym napisie ma ord(c)>100
    if ord(i) < 100: #to nie wypisze nic, ale zmieniajac q na Q juz wypisze
        print(i)    # Q bo ma wartosc 81


for i in "Qwerty":
    if ord(i) < 100:
        print(i)


print("Wartosc ord(Q):", ord("Q"))

print("c)")
print("Dany kod:")
for i in "axby": print (ord(i)) if ord(i) < 100 else i
# kod dziala ale chyba nie do konca tak jaki byl zamiar
# zeby bylo bardziej czytelnie, powinno sie to zapisywac
# tak jak ponizej, i jesli w zamiarze ten kod mial
# wypisywac ord(i) jesli <100 a w przeciwnym wypadku
# mial wypisywac litere czyli i, to dany kod nie dziala
# prawidlowo, ponizej poprawna wersja
print ("Moja poprawka:")
for i in "axby":
    if ord(i) < 100:
        print(ord(i))
    else:
        print (i)
