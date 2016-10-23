#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
while(True):
    number = input("Podaj liczbe rzeczywista")
    try:
        number2 = float(number)
        result = (pow(number2, 3))
        print("(%s,%s)" % (number, result))
    except ValueError:
        if number == "stop":
            break
        else:
            print("Blad!")

