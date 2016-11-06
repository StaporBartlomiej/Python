#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

def odwracanie(L,left,right):
    while left < right:  #swap
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1
    return L
def odwracanieRek(L,left,right):
    if (left < right):
        L[left], L[right] = L[right], L[left]
        return odwracanieRek(L, left+1, right-1)
    else:
        return L
test = [1, 2, 3, 4, 5]
test2 = [1, 2, 3, 4, 5]
print(test)
od = int(input("Odwroc liste(numerowana od 0):\nOd:"))
do = int(input("Do:"))
print("Iterative:\n",odwracanie(test,od,do))
print("Recursive:\n",odwracanieRek(test2,od,do))


