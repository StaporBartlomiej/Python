#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

def sum_seq(sequence):
    result = 0
    for item in (sequence):
        if (isinstance(item,(list,tuple))):
            result += sum_seq(item)
        else:
            result += item
    return result



seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]

print(seq)

print(sum_seq(seq))
