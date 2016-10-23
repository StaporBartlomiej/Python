#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

print("Aby zatrzymac program, wpisz 'stop' jako arguement x badz y")
while(True):
    wejx = input("Podaj x(pionowo):")
    wejy = input("Podaj y(poziomo):")

    try:
        x = int(wejx)
        y = int(wejy)
        up = "+---"
        mid = "|   "
        bot = up
        S = ""
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
            print(result)
        else:
            result3 = result2 * x + bot
            print(result3)
    except ValueError:
        if wejx == "stop" or wejy == "stop":
            break
        else:
            print("Blad!")





