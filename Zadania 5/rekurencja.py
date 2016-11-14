#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

def factorial(n):
    temp=1
    if n in (0,1):
        return 1
    else:
        for i in range(2,n+1):
          temp = temp * i
    return temp


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

