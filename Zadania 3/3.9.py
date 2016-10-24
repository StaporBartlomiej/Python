#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

lista = [[],[4],(1,2),[3,4],(5,6,7)]
result = []

for i in lista:
    result.append(sum(i))

print(result)