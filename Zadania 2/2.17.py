#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
line = "Lorem ipsum dolor sit amet\nconsectetur adipiscing elit.\nEtiam blandit luctus consectetur."
lista = line.split()

print ("Sorted by alphabetical order:\n",sorted(lista,key = str.lower))
print ("\nSorted by lenght:\n",sorted(lista,key = len ))
