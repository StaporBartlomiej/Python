#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

def Figures(wejx,wejy):
    x = int(wejx)
    y = int(wejy)
    up = "+---"
    mid = "|   "
    bot = up
    y = y - 1

    for i in range(y):
        up = up + "+---"
        mid = mid + "|   "
        bot = bot + "+---"
        if (i == y - 1):
            up = up + "+"
            mid = mid + "|"
            bot = bot + "+"
    if y < 1:
        up = up + "+"
        mid = mid + "|"
        bot = bot + "+"
    result = up + "\n" + mid + "\n" + bot
    result2 = up + "\n" + mid + "\n"

    if x == 1:
        return result
    else:
        result3 = result2 * x + bot
        return result3

def Ruler(lenght):
    S = ""
    underRuler = ""
    for i in range(lenght):

        S = S + "|...."
        if i >= 10 and i < 100:
            underRuler = underRuler + str(i) + "   "
        elif i >= 100 and i <= 1000:
            underRuler = underRuler + str(i) + "  "
        else:
            underRuler = underRuler + str(i) + "    "
        if (i == lenght - 1):
            S = S + "|"
        if lenght == 1:
            S = "|"
            underRuler = "0"
    result = S + "\n" + underRuler + str(i + 1)

    return result


choice = int(input("Wybierz jedno:\n1. Linijka\n2. Figury"))
if (choice == 1):
    lenght = int(input("Podaj dlugosc miarki"))
    print(Ruler(lenght))
elif (choice == 2):
    wejx = int(input("Podaj x(pionowo):"))
    wejy = int(input("Podaj y(poziomo):"))
    print(Figures(wejx,wejy))


