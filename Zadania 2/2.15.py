#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

L = [1,2,3,4,5]
S = ""
Result = S.join(str(x) for x in L) # str() - Return a string version of object
print (Result)

#or simply

B = ['1','2','3','4','5']
D = ""
Result2 = D.join(B)
print("\nSecond way\n",Result2)
