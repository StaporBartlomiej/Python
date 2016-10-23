#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

line = "Lorem ipsum dolor sit amet\nconsectetur adipiscing elit.\nEtiam blandit luctus consectetur."
lista = line.split()
listaA = []
listaB = []
resultA = ""
resultB = ""
print ("Line:\n",line,"\n")
for i in range(len(lista)):
    listaA.append((lista[i])[:1])
resultA = "".join(listaA)
print ("Napis stworzony z pierwszych znakow wyrazow z wiersza line:\n",resultA)


for i in range(len(lista)):
    listaB.append((lista[i])[-1])
resultB = "".join(listaB)
print ("Napis stworzony z ostatnich znakow wyrazow z wiersza line:\n",resultB)
