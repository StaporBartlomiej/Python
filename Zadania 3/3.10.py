#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
import roman

dictionary = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

def roman2Arabic(number):
    result2 = roman.fromRoman(number)
    return result2

def roman2Arabic2(number):
    result = []
    for i in range(len(number)):
        if(number[i] == "I"):
            result.append(dictionary.get("I"))
        elif (number[i] == "V"):
            result.append(dictionary.get("V"))
        elif (number[i] == "X"):
            result.append(dictionary.get("X"))
        elif (number[i] == "L"):
            result.append(dictionary.get("L"))
        elif (number[i] == "C"):
            result.append(dictionary.get("C"))
        elif (number[i] == "D"):
            result.append(dictionary.get("D"))
        elif (number[i] == "M"):
            result.append(dictionary.get("M"))
    return(sum(result))






number = input("Podaj liczbe rzymska:\n")
print("a)",roman2Arabic(number))
print("b)",roman2Arabic2(number))
