#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

line = "Lorem ipsum dolor sit amet\nconsectetur adipiscing elit.\nEtiam blandit luctus consectetur."
listaWyrazow = line.split()
MaxLength = len(listaWyrazow[0])

for i in range(len(listaWyrazow)): #Znajduje maksymalna dlugosc wyrazu
    if MaxLength < len(listaWyrazow[i]):
        MaxLength = len(listaWyrazow[i])


#print (MaxLength)
for i in range(len(listaWyrazow)): # Znajduje wyraz o maksymalnej dlugosci
    if MaxLength == len(listaWyrazow[i]):
        print ("Najdluzszy wyraz to: ",listaWyrazow[i],"\nJego dlugosc to: ",len(listaWyrazow[i]))
    
