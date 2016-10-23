#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

#Dziala poprawnie dla dowolnej liczby calkowitej <= 1000

S = ""
lenght = int(input("Podaj dlugosc miarki"))
underRuler = ""
for i in range(lenght):

    S = S + "|...."
    if i >= 10 and i < 100:
        underRuler = underRuler + str(i) + "   "
    elif i >= 100 and i <= 1000:
        underRuler = underRuler + str(i) + "  "
    else:
        underRuler = underRuler + str(i) + "    "
    if(i == lenght-1):
        S = S + "|"
    if lenght == 1:
        S = "|"
        underRuler = "0"
result = S + "\n" + underRuler  + str(i+1)
#result = result[:75]
print(result)
