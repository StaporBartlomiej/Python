#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
def fibonacci(n):
    if(n == 0):
        return 0
    else:
        x = 0
        y = 1
        for i in range(1,n):
            z = (x + y)
            x = y
            y = z
        return y

wej = int(input("Podaj n:\n"))
for i in range(wej+1):
    print(fibonacci(i))
