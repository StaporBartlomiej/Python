#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

def silnia_iter(n):
    temp=1
    if n in (0,1):
        return 1
    else:
        for i in range(2,n+1):
          temp = temp * i
    return temp



wej = int(input("Podaj n:\n"))
print(silnia_iter(wej))