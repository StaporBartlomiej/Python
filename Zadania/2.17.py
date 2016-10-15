#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
line = "Lorem ipsum dolor sit amet\nconsectetur adipiscing elit.\nEtiam blandit luctus consectetur."
lista = line.split()
def lengthCompare(x , y):
    if x < y:
        return y
    elif x > y:
        return x
    else:
        return 0

print ("Sorted by alphabetical order:\n",sorted(lista,key = str.lower))
print ("\nSorted by lenght:\n",sorted(lista,key = len ))
