#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

listA = ["a","b","c","d"]
listB = ["c","d","e","f"]
result = []

for i in listA:
    if (i in listB):
        result.append(i)

print("a)",result)
result2 = []
for i in listA:
    if (i not in result2):
        result2.append(i)

for i in listB:
    if (i not in result2):
        result2.append(i)

print("b)",result2)